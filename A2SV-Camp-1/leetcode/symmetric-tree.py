# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def c(l, r):
            if l and r:
                if l.val!=r.val: return False
                return c(l.left,r .right) and c(l.right, r.left)

            elif (l and not r) or (r and not l): return False
            return True
        # print(c(root, root))
        # print(ans)
        return c(root,root)