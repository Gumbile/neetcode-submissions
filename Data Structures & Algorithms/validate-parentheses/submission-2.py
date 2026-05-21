class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(','{','[']


        for char in s:
            
            if char in open_brackets:
                stack.append(char)
            elif char == ')' and stack and stack[-1] == open_brackets[0]:
                stack.pop()
            elif char == '}' and stack and stack[-1] == open_brackets[1]:
                stack.pop()
            elif char == ']' and stack and stack[-1] == open_brackets[2]:
                stack.pop()
            else:
                return False

        if stack :
            return False
        return  True