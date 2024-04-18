# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads=[]
        for idx,head in enumerate(lists):
            if head: heads.append((head.val, idx, head))

        heapify(heads)
        dummy=res=ListNode()

        while heads:
            val, idx, cur = heappop(heads)
            res.next=ListNode(val)
            res=res.next

            if cur.next: heappush(heads, (cur.next.val, idx, cur.next))

        return dummy.next

