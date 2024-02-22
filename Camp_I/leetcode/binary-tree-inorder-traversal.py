# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def recurse(node):
            if not node:
                return
            recurse(node.left)
            arr.append(node.val)
            recurse(node.right)
            return
        recurse(root)
        return arr