# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(cur1,cur2):
            if cur1 and cur2:
                cur1.val+=cur2.val
                cur1.left=merge(cur1.left,cur2.left)
                cur1.right=merge(cur1.right,cur2.right)
                return cur1
            elif cur2 and not cur1: 
                return cur2
            return cur1
        
        return merge(root1,root2)