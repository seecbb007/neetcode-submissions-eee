class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in '+-*/':
                a = stack.pop()
                b = stack.pop()

                if t == '+':
                    stack.append(b + a)
                if t == '-':
                    stack.append(b - a)

                if t == '*':
                    stack.append( b * a)

                if t == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[-1]