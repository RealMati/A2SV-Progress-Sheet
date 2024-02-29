# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=cur=ListNode()
        dummy.next=head
        
        lConnect=rConnect=None
        idx=0

        while cur:
            if idx==left-1:
                lConnect=cur
            elif idx==right+1:
                rConnect=cur
        
            cur=cur.next
            idx+=1

        prev=None
        cur=left=lConnect.next
        # lConnect.next=None

        while cur!=rConnect:
            nextt=cur.next
            cur.next=prev
            prev=cur
            cur=nextt

        lConnect.next=prev
        left.next=cur
        return dummy.next
