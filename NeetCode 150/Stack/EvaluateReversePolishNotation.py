# O(n) solution with stack.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                stack.append(-1 * (stack.pop() - stack.pop()))

            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "/":
                prev = stack.pop()
                prev_prev = stack.pop()
                stack.append(int(prev_prev / prev))

            else:
                stack.append(int(token))

        return stack[0]


# Fall 2023 Solution. Similar to above but not optimized:


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                a, b = int(stack[-2]), int(stack[-1])
                res = a + b
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == "-":
                a, b = int(stack[-2]), int(stack[-1])
                res = a - b
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == "*":
                a, b = int(stack[-1]), int(stack[-2])
                res = a * b
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == "/":
                a, b = int(stack[-2]), int(stack[-1])
                res = int(a / b)
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(token)

        return int(stack[0])
