# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        cur=head

        while cur:
            size+=1
            cur=cur.next
        
        middle=size//2
        idx=0
        cur=head
        print(size,middle)
        while idx<middle:
            idx+=1
            cur=cur.next
        return cur