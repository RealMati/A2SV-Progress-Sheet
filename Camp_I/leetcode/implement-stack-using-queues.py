class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class MyStack:
    def __init__(self):
        self.head = Node(None)
    def push(self, x: int) -> None:
        newnode = Node(x)
        newnode.prev = self.head
        self.head.next = newnode
        self.head = self.head.next
    def pop(self) -> int:
        value = self.head.val
        self.head = self.head.prev
        self.head.next = None
        return value
    def top(self) -> int:
        return self.head.val
    def empty(self) -> bool:
        if self.head.val:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()