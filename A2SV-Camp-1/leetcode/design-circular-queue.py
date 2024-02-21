class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyCircularQueue:
    def __init__(self, k: int):
        self.size=k
        self.front=None
        self.rear=None
        self.curSize=0

    def enQueue(self, value: int) -> bool:
        if self.curSize==self.size: return False
        node=Node(value)

        if self.curSize==0:
            self.rear=node
            self.front=node
            self.curSize+=1
            return True

        self.rear.next=node
        self.rear=node
        self.curSize+=1
        return True

    def deQueue(self) -> bool:
        if self.curSize>0:
            if self.rear==self.front: self.rear=None
            self.front=self.front.next
            self.curSize-=1
            return True
        else: return False

    def Front(self) -> int:
        return self.front.val if self.front else -1

    def Rear(self) -> int:
        return self.rear.val if self.rear else -1
        
    def isEmpty(self) -> bool:
        return self.curSize==0

    def isFull(self) -> bool:
        return self.curSize==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()