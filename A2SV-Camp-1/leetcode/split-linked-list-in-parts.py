# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        step=k
        cur=c=head
        res=[]
        size=0
        
        while c:
            size+=1
            c=c.next

        for i in range(k):
            space=math.ceil(size/k)
            size-=space
            k-=1
            res.append(cur)

            for i in range(space-1):
                if cur and cur.next: cur=cur.next
                else: 
                    cur=None
                    break
            if cur: 
                temp=cur.next
                cur.next=None
                cur=temp           
                
        return res
            
