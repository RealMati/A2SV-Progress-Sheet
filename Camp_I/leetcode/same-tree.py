# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        count = 0
        def issame(p,q):
            nonlocal count
            if not p and q:
                count+=1
                return
            if not q and p:
                count+=1
                return
            if not q and not p:
                return
            if p.val!=q.val:
                count+=1
            issame(p.left,q.left)
            issame(p.right,q.right)
            return
        issame(p,q)
        if count:
            return False
        return True