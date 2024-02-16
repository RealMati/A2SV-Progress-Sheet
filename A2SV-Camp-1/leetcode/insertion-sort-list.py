# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head

        while cur.next:
            node=cur.next
            if cur.next.val<cur.val:
                cur.next=cur.next.next
                currr=head
                if node.val<=head.val:
                    node.next=currr 
                    head=node
                    continue
                    
                while currr.next:
                    if node.val<=currr.next.val:
                        node.next=currr.next
                        currr.next=node
                        break
                    else:
                        currr=currr.next
            else:
                cur=cur.next
        
        return head

