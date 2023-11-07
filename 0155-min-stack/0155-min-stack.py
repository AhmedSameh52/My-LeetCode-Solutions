class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        lowest = self.stack[0]
        for i in range(0, len(self.stack)):
            if self.stack[i] < lowest:
                lowest = self.stack[i]
        # if lowest != 99999999:
        # self.stack.remove(lowest)
        # self.stack.append(lowest)
        return lowest


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()