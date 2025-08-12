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

# or 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"]":"[", ")":"(", "}":"{"}
        for b in s:
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
        
            