# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[float('-inf')]
        def validate(cur):
            if cur:
                cur.left=validate(cur.left)
                ans.append(cur.val)
                cur.right=validate(cur.right)
                return cur

        validate(root)
        for i in range(len(ans)-1):
            if ans[i]>=ans[i+1]: return False
        return True