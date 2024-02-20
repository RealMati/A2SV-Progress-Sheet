# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(head):
            if head == None or head.next == None:
                return head
            p1 = head
            p2 = head.next
            p3 = head.next.next
            p1.next = p3
            p2.next = p1
            if p3!=None:
                p1.next = recurse(p3)
            return p2
        return recurse(head)
        