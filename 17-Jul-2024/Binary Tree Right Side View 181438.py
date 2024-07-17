# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q=deque([root])
        res=[]

        while q:
            for i in range(len(q)):
                cur=q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(cur.val)

        return res
                

                