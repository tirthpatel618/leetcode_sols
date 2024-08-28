#cheat soltuin, want to try it in cpp

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(' ')
        while "" in s_list:
            s_list.remove("")
        return len(s_list[-1])