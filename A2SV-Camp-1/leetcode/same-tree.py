# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(cur1,cur2):
            if cur1 and cur2:
                if cur1.val!=cur2.val: return False
                return traverse(cur1.left,cur2.left) and traverse(cur1.right,cur2.right)
            if (cur1 and not cur2) or (cur2 and not cur1): return False
            return True  
            
        return traverse(p,q)

