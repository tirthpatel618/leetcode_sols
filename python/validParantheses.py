#also very proud

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            elif len(stack) == 0 or brackets[stack.pop()] != i:
                return False
        return len(stack) == 0        