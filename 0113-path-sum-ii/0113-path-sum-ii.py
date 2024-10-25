# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res=[]

        def dfs(cur, summ, path):
            
            if not cur.left and not cur.right and summ==targetSum:
                ans=path[:]
                res.append(ans)
            
            if cur.left:
                path.append(cur.left.val)
                summ+=cur.left.val
                dfs(cur.left, summ, path)
                path.pop()
                summ-=cur.left.val
            
            if cur.right:
                path.append(cur.right.val)
                summ+=cur.right.val
                dfs(cur.right, summ, path)
                path.pop()
                summ-=cur.right.val
        
            return res

        return dfs(root, root.val, [root.val])
        