# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        res=0
        visited=set()

        def dfs(cur, summ, size):
            nonlocal res

            if (cur, summ, size) in visited: return res
            visited.add((cur, summ, size))
            
            if summ==targetSum:
                res+=1
            
            if cur.left:
                summ+=cur.left.val
                dfs(cur.left, summ, size+1)
                dfs(cur.left, cur.left.val, 1)
                summ-=cur.left.val
            
            if cur.right:
                summ+=cur.right.val
                dfs(cur.right, summ, size+1)
                dfs(cur.right, cur.right.val, 1)
                summ-=cur.right.val
        
            return res

        return dfs(root, root.val, 1)
        