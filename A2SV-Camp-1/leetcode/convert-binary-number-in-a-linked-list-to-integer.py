# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        size=res=0
        cur=head

        while cur:
            size+=1
            cur=cur.next
            
        cur=head
        while cur:
            res+=(2**(size-1))*int(cur.val)
            cur=cur.next
            size-=1

        return res