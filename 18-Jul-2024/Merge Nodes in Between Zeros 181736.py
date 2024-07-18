# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head.next
        prevZero=head
        summ=0

        while cur:
            if cur.val==0 and summ>0:
                prevZero.next=cur
                cur.val=summ
                summ=0
                prevZero=cur
            else:
                summ+=cur.val
            cur=cur.next

        return head.next
            