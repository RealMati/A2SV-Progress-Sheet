# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxdepths(node):
            if not node:
                return 0
            return max(1+maxdepths(node.left),1+maxdepths(node.right))
        return maxdepths(root)