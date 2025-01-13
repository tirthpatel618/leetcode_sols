class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26
        length = 0
        for char in s:
            freq[ord(char) - ord("a")] += 1
        
        for number in freq:
            if number == 0:
                continue
            if number % 2 == 0:
                length += 2
            else:
                length += 1
        return length

#medium but pretty easy jan 13