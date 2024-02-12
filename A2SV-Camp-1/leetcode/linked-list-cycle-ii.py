# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        intersect=False
        dummy=ListNode()
        dummy.next=head
        slow=fast=dummy

        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                intersect=True
                break
        if intersect==False:
            return 

        again=dummy

        while again!=fast:
            again=again.next
            fast=fast.next
        
        return fast
            