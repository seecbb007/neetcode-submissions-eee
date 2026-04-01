class Solution:
    def isValid(self, s: str) -> bool:
        bracketmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for char in s:
            if char not in bracketmap:
                stack.append(char)
            else:
                if not stack or  stack[-1] != bracketmap[char]:
                    return False

                stack.pop()

        return not stack
