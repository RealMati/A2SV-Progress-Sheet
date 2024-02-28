# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        res=None
        ct=0
        def c(cur):
            nonlocal res, ct
            if cur:
                if ct>=k:
                    return
                cur.left=c(cur.left)
                ct+=1
                # print(ct,cur.val)
                if ct==k and not res:
                    res = cur.val
                    return
                cur.right=c(cur.right)
                return cur
        c(root)
        # print(res)
        return res