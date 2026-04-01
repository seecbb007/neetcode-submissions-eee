class Solution:
    def isValid(self, s: str) -> bool:
        dictt={')':'(',
        '}':'{',
        ']':'['
        }
        stack = []
        for char in s:
            if char not in dictt:
                stack.append(char)
            else:
                if not stack or stack[-1] != dictt[char]:
                    return False
                stack.pop()
        return not stack                


        