# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=TreeNode(val)
        if not root: return node
        def ins(cur):
            if not cur:
               return node
            if val<cur.val: 
                cur.left=ins(cur.left)
                return cur
            if val>cur.val:
                cur.right=ins(cur.right)
                return cur
        return ins(root)
        
