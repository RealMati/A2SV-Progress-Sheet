# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def recurse(node):
            if not node:
                return
            arr.append(node.val)
            recurse(node.left)
            recurse(node.right)
            return
        recurse(root)
        return arr