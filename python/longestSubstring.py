#my proudest one yet 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in chars:
                  chars.remove(s[left])
                  left +=1
            chars.add(s[right])
            maxlen = max(maxlen, right - left + 1)
        return maxlen