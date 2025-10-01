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
    
# or 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = {}
        for r, ch in enumerate(s):
            if ch in seen:
                l = max(seen[ch]+1, l)
            seen[ch] = r
            max_len = max(max_len, r-l+1)
        return max_len
                
        