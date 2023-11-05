# Obviosuly using .pop() in MinStack.pop() defeats the purpose
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        # self.stack.pop()
        """Or we can use del"""
        del self.stack[len(self.stack) - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Fall 2023 solution
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # O(1)

    def pop(self) -> None:
        del self.stack[-1]
        # O(1)

    def top(self) -> int:
        if not self.stack:
            return None
        item = self.stack[-1]
        del self.stack[-1]
        return item
        # O(1)

    def getMin(self) -> int:
        return min(self.stack, default=-1)
