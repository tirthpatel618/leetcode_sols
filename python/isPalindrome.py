#cheat solution, should probably do in c++

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)[::-1]
        print(num)
        return num == str(x)