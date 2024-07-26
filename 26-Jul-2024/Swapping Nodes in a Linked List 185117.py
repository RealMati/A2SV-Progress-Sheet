# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur1=cur2=head
        
        ind=0
        cur=None
        while cur1:
            if (ind+1)==k:
                cur=cur1

            cur1=cur1.next
            ind+=1
        
        i=1
        while cur2 and i!=(ind-k+1):
            cur2=cur2.next
            i+=1
        
        cur.val,cur2.val=cur2.val,cur.val
        return head
        


        
        



