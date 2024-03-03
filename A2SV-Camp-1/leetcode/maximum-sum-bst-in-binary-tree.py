# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxx=0

        def c(cur):
            nonlocal maxx

            if not cur.left and not cur.right:
                maxx=max(maxx, cur.val)
                return cur.val, cur.val, cur.val
            
            lsum, lmin, lmax = 0, cur.val, float('-inf')
            if cur.left:
                lsum, lmin, lmax = c(cur.left)
            
            rsum, rmin, rmax = 0, float('inf'), cur.val
            if cur.right:
                rsum, rmin, rmax = c(cur.right)
            
            if lmax<cur.val<rmin:
                summ= lsum+cur.val+rsum
                maxx=max(summ, maxx)
                return summ, lmin, rmax
            else:
                return 0, float('-inf'), float('inf')
        c(root)
        return maxx

