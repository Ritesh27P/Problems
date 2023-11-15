class Solution:
    def evalRPN(self, tokens) -> int:
        notation = ['*', '+', '-', '/']

        stack = []
        for i in tokens:
            if i in notation:
                v1 = stack.pop()
                v2 = stack.pop()
                if i == '*':
                    stack.append(v1*v2)
                elif i == '+':
                    stack.append(v1+v2)
                elif i == '-':
                    stack.append(v2-v1)
                elif i == '/':
                    stack.append(int(v2/v1))
            else:
                stack.append(int(i))
        return stack[-1]
        