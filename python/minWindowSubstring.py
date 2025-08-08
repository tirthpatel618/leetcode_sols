class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        hashT, window = {}, {}
        for c in t:
            hashT[c] = 1 + hashT.get(c, 0)
        have = 0
        need = len(hashT) #treat the chars as distinct now since we track their counts
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in hashT and window[c] == hashT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in hashT and window[s[l]] < hashT[s[l]]:
                    have -= 1
                l+= 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""      
        
#hard problem. neat solution that i had to look at solution for but (maybe) couldve came up with myself
