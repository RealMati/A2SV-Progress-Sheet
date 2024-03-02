# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxx = 0
        ans = []

        def c(cur):
            nonlocal maxx
            ans.append(cur.val)
            if cur.left:
                c(cur.left)
                ans.pop()
            maxx=max(maxx, max(ans)-min(ans))
            if cur.right:
                c(cur.right)
                ans.pop()
            maxx=max(maxx, max(ans)-min(ans))

            if not cur.left and cur.right:
                maxx=max(maxx, max(ans)-min(ans))
        c(root)
        return maxx
