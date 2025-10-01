def find_shortest_subarray_with_all_values(arr):
    if not arr:
        return []

    unique_values = set(arr)
    required_count = len(unique_values)
    value_count = collections.defaultdict(int)

    left = 0
    min_length = float('inf')
    min_subarray = []

    for right in range(len(arr)):
        value_count[arr[right]] += 1

        while len(value_count) == required_count:
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                min_subarray = arr[left:right + 1]

            value_count[arr[left]] -= 1
            if value_count[arr[left]] == 0:
                del value_count[arr[left]]
            left += 1

    return min_subarray