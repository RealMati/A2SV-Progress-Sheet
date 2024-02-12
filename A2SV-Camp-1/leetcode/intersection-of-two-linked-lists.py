# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sett=set()

        while headA:
            sett.add(headA)
            headA=headA.next

        while headB:
            if headB in sett:
                return headB
            headB=headB.next
