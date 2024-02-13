# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=cur=ListNode()
        dummy.next=head
        oddHead=odd=head

        if not odd:
            return odd
        while odd.next:
            if cur.next: cur.next=odd.next
            cur=cur.next
            
            if odd.next.next: odd.next=odd.next.next
            else: break
            odd=odd.next
        if cur.next and not cur.next.next:  cur.next=None
        # print(oddHead,dummy.next)
        # print("S",cur)
        odd.next=dummy.next
        return oddHead

