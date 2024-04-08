# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q=deque([root])
        res=[]
        while q:
            ans=[]
            for i in range(len(q)):
                cur=q.popleft()
                ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)            
            res.append(ans)
        # print(res)
        return res