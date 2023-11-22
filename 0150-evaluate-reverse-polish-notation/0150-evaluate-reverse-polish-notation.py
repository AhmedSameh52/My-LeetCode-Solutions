class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for symbol in tokens:
            if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' :
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if symbol == '+':
                    stack.append(num1 + num2)
                elif symbol == '-':
                    stack.append(num1 - num2)
                elif symbol == '*':
                    stack.append(num1 * num2)
                elif symbol == '/':
                    stack.append(num1 / num2)
            else:
                stack.append(symbol)
        return int(stack.pop())