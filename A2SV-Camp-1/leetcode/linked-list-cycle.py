# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett=set()
        cur=head
        
        while cur:
            sett.add(id(cur))
            if id(cur.next) in sett:
                return True
            cur=cur.next
        return False
