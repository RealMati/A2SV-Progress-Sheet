# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res=0
        parent={}
        leafs=[]

        def traverse(cur):
            if cur:
                if not cur.left and not cur.right:
                    leafs.append(cur)

                if cur.left:
                    parent[cur.left]=cur
                    traverse(cur.left)
                if cur.right:
                    parent[cur.right]=cur
                    traverse(cur.right)

        traverse(root)


        def dfs(cur, step):
            nonlocal res, visited

            if step>distance or cur in visited:
                return 0

            if not cur.left and not cur.right and step!=0:
                res+=1
                return 0

            visited.add(cur)
            if cur.left: 
                dfs(cur.left, step+1)
            
            if cur.right:
                dfs(cur.right, step+1)
            
            if cur in parent:
                dfs(parent[cur], step+1)
            

        for leaf in leafs:
            visited=set()
            dfs(leaf, 0)
        
        return res//2