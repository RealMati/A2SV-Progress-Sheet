# Problem: Middle of a Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if not fast:
            return 
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        return slow
