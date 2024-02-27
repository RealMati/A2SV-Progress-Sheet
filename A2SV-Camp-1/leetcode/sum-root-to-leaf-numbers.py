# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        ans=[]
        def c(cur):
            nonlocal res
            if cur:
                ans.append(str(cur.val))
                if not cur.left and not cur.right:
                    res+=(int("".join(ans)))
                cur.left=c(cur.left)
                cur.right=c(cur.right)
                ans.pop()
                return cur
        c(root)
        return res
