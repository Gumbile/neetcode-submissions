class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')':'(','}':'{',']':'['}

        for char in s:
            if char in brackets_map:
                top = stack.pop() if stack else '#'

                if top != brackets_map[char]:
                    return False
            else:
                stack.append(char)

        return not stack