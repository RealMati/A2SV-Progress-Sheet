# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root: return []
        stack=[root]
        while stack:
            cur=stack[-1]
            ans.append(cur.val)
            stack.pop()
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return ans