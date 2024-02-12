class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        idx=0
        cur=self.head
        # print(index,self.size)
        if index>=self.size:
            return -1
        while idx<index and cur.next:
            cur=cur.next
            idx+=1
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
        self.size+=1
        # print(self.size)

    def addAtTail(self, val: int) -> None:
        if self.head==None:
            self.addAtHead(val)
            return 
        newNode=Node(val)
        cur=self.head
        while cur.next:
            cur=cur.next

        cur.next=newNode
        self.size+=1
        # print("tail",self.size)
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val) 
            return 
        if index>self.size:
            return 
        idx=0
        newNode=Node(val)
        cur=self.head
        
        while idx+1<index and cur.next:
            cur=cur.next
            idx+=1
        
        if cur.next: newNode.next=cur.next
        cur.next=newNode
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head=self.head.next
        else:
            if index>self.size-1: return 
            idx=0
            cur=self.head
            
            while idx+1<index and cur.next:
                cur=cur.next
                idx+=1
            
            cur.next=cur.next.next
        self.size-=1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)