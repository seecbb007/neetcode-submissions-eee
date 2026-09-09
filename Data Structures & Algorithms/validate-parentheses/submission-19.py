class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chardict = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char not in chardict:
                stack.append(char)
            else:
                if not stack or stack[-1] != chardict[char]:
                    return False

                stack.pop()
        return not stack
        