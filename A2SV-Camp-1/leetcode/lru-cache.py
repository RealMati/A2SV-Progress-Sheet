class DLL:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic={}
        self.head=None
        self.tail=None
        self.size=0

    def get(self, key: int) -> int:
        # print(key,"before get", self.head.key,self.head.next.key,self.tail.key)
        if key not in self.dic: return -1
        
        node=self.dic[key]
        if self.dic[key]==self.head:
            return self.head.val
        
        before=None
        after=None
        if self.dic[key].prev: before=self.dic[key].prev
        if self.dic[key].next: after=self.dic[key].next

        if after: 
            after.prev=before
        if before:
            before.next=after
        if self.dic[key]==self.tail and self.dic[key].prev:
           self.tail=self.dic[key].prev
        elif not self.dic[key].prev and not self.dic[key].next:
            self.tail=self.dic[key]
            self.head=self.dic[key]

        node.prev=None
        node.next=self.head
        self.head.prev=node
        self.head=node

        # print(key, "after get", self.head.key,self.head.next.key,self.tail.key)
        # print(key, "get" ,self.dic,self.head.key,self.head.next.key)
        return self.dic[key].val


    def put(self, key: int, value: int) -> None:

        # print("before put",self.head,self.tail)
        if key not in self.dic:
            newNode=DLL(key,value)
            self.dic[key]=newNode

            if self.size==0:
                self.head=newNode
                self.tail=newNode
                self.size+=1
            elif self.size<self.capacity:
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
                self.size+=1
            elif self.size==self.capacity:
                if self.tail.key in self.dic: del self.dic[self.tail.key]

                if self.tail.prev: 
                    self.tail=self.tail.prev
                self.tail.next=None

                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            
        else:
            self.dic[key].val=value

            node=self.dic[key]
            if node==self.head:
                return
            before=None
            after=None
            if self.dic[key].prev: before=self.dic[key].prev
            if self.dic[key].next: after=self.dic[key].next

            if after: after.prev=before
            if before: before.next=after
            if not after and before:
                self.tail=before
            elif not after and not before:
                self.tail=self.dic[key] 

            node.prev=None
            node.next=self.head
            self.head.prev=node
            self.head=node
        # print("after-put", self.head.key,self.head,self.tail.key)
        #
        # print("put")
        # pr=[]
        # cur=self.head
        # while cur:
        #     pr.append(cur.key)
        #     cur=cur.next
        # print(pr)
        ##



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)