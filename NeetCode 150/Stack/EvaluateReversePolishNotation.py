#O(n) solution with stack. 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif token == "-":
                stack.append(-1*(stack.pop() - stack.pop()))
            
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif token == "/":
                prev = stack.pop()
                prev_prev = stack.pop()
                stack.append(int(prev_prev/prev))
            
            else:
                stack.append(int(token))
        
        return stack[0]
