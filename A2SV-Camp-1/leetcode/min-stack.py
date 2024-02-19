class MinStack:

    def __init__(self):
        self.minstack=deque()
        self.stack=deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and val<=self.minstack[-1]: self.minstack.append(val)
        elif not self.minstack: self.minstack.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinminStack object will be instantiated and called as such:
# obj = MinminStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()