# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ=0
        def c(cur):
            nonlocal summ
            if cur:
                if low<=cur.val<=high:
                    summ+=cur.val
                c(cur.left)
                c(cur.right)
            return summ
        return c(root)