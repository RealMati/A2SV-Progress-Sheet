# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=cur=lastBig=ListNode(float('inf'))
        dummy.next = head
        lessHead = less=ListNode()
        connect = None
        lastSmall=None
        while cur and cur.next:
            lastBig=cur
            while cur.next and cur.next.val<x:
                less.next=cur.next
                cur=cur.next
                less=cur
                # print(less.val)
            lastBig.next=cur.next
            cur=cur.next
        # print(lessHead)
        # print(dummy)
        less.next=dummy.next
        return lessHead.next
           