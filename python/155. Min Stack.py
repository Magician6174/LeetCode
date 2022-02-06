class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_value = None

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_value = val
            self.min_stack.append(val)
            return
        if val < self.min_value:
            self.min_stack.append(2*val-self.min_value)
            self.min_value = val
        else:
            self.min_stack.append(val)
    def pop(self) -> None:
        if self.min_stack[-1] < self.min_value:
            self.min_value = 2 * self.min_value - self.min_stack[-1]
        self.min_stack.pop()

    def top(self) -> int:
        if self.min_stack[-1] > self.min_value:
            return self.min_stack[-1]
        else:
            return self.min_value

    def getMin(self) -> int:
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
