# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        idx=0
        dic={}
        cur=head
    
        while cur:
            dic[idx]=cur
            idx+=1  
            cur=cur.next
        gap=idx-1
        
        for i in range(idx//2):
            if dic[i].val!=dic[i+gap].val:
                return False
            gap-=2

        return True
            