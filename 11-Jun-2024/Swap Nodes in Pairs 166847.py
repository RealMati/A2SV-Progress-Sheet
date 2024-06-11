# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=prev=ListNode()
        dummy.next=cur=head
        
        if not head: return head 
        def swap(prev,cur):
            if not cur or not cur.next: return dummy.next
            node=cur.next
            cur.next=node.next
            node.next=cur
            prev.next=node

            return swap(cur,cur.next)
        
        return swap(prev,cur)