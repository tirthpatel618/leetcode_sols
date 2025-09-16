#testing small parts of solutions
def max_array_length(r):
    """
    Find the maximum possible length of array A given constraints:
    - All elements must be in range [1, r)
    - For any i>=1: A[i] = 2*A[i-1] OR A[i] = A[i-1] + 6
    
    Args:
        r: Upper bound (exclusive) for array elements
    
    Returns:
        Maximum possible length of array A
    """
    if r <= 1:
        return 0
    
    # dp[v] = maximum length of array ending with value v
    dp = {}
    
    # Initialize: any value in [1, r) can be the first element
    for start_val in range(1, r):
        dp[start_val] = 1
    
    # Keep track of maximum length found
    max_length = 1
    
    # Continue building arrays until no new values can be added
    changed = True
    while changed:
        changed = False
        new_dp = dp.copy()
        
        for val, length in dp.items():
            # Try doubling
            next_val = 2 * val
            if next_val < r:
                if next_val not in new_dp or new_dp[next_val] < length + 1:
                    new_dp[next_val] = length + 1
                    max_length = max(max_length, length + 1)
                    changed = True
            
            # Try adding 6
            next_val = val + 6
            if next_val < r:
                if next_val not in new_dp or new_dp[next_val] < length + 1:
                    new_dp[next_val] = length + 1
                    max_length = max(max_length, length + 1)
                    changed = True
        
        dp = new_dp
    
    return max_length


def find_optimal_sequence(r):
    """
    Find an actual sequence that achieves the maximum length.
    
    Args:
        r: Upper bound (exclusive) for array elements
    
    Returns:
        A list representing an optimal sequence
    """
    if r <= 1:
        return []
    
    # Store the best sequence ending at each value
    sequences = {}
    
    # Initialize with all possible starting values
    for start_val in range(1, r):
        sequences[start_val] = [start_val]
    
    # Build sequences
    changed = True
    while changed:
        changed = False
        new_sequences = sequences.copy()
        
        for val, seq in sequences.items():
            # Try doubling
            next_val = 2 * val
            if next_val < r:
                new_seq = seq + [next_val]
                if (next_val not in new_sequences or 
                    len(new_sequences[next_val]) < len(new_seq)):
                    new_sequences[next_val] = new_seq
                    changed = True
            
            # Try adding 6
            next_val = val + 6
            if next_val < r:
                new_seq = seq + [next_val]
                if (next_val not in new_sequences or 
                    len(new_sequences[next_val]) < len(new_seq)):
                    new_sequences[next_val] = new_seq
                    changed = True
        
        sequences = new_sequences
    
    # Find the longest sequence
    max_seq = []
    for seq in sequences.values():
        if len(seq) > len(max_seq):
            max_seq = seq
    
    return max_seq


# Test the solution
if __name__ == "__main__":
    # Test cases
    test_cases = [10, 20, 50, 100, 200]
    
    for r in test_cases:
        max_len = max_array_length(r)
        optimal_seq = find_optimal_sequence(r)
        
        print(f"r = {r}:")
        print(f"  Maximum length: {max_len}")
        print(f"  Example sequence: {optimal_seq}")
        print(f"  Verification: Length = {len(optimal_seq)}")
        
        # Verify the sequence follows the rules
        if len(optimal_seq) > 1:
            valid = True
            for i in range(1, len(optimal_seq)):
                if optimal_seq[i] != 2 * optimal_seq[i-1] and \
                   optimal_seq[i] != optimal_seq[i-1] + 6:
                    valid = False
                    break
            print(f"  Sequence is valid: {valid}")
        print()