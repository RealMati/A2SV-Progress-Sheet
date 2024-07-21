# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent={}
        res=""
        startNode=None

        def traverse(cur):
            nonlocal startNode
            if cur:
                if cur.val==startValue:
                    startNode=cur

                if cur.left:
                    parent[cur.left.val]=cur
                    traverse(cur.left)
                if cur.right:
                    parent[cur.right.val]=cur
                    traverse(cur.right)

        traverse(root)

        def dfs(cur, steps, visited):
            nonlocal res
            if cur:
                # print(cur.val, steps)
                if cur.val == destValue:
                    res="".join(steps)
                    # print(res)
                    return steps

                visited.add(cur.val)
                if cur.left and cur.left.val not in visited:
                    steps.append('L')
                    dfs(cur.left, steps, visited)
                    steps.pop()

                if cur.right and cur.right.val not in visited:
                    steps.append('R')
                    dfs(cur.right, steps, visited)
                    steps.pop()
                
                if cur.val in parent and parent[cur.val].val not in visited:
                    steps.append('U')
                    dfs(parent[cur.val], steps, visited)
                    steps.pop()

   
        dfs(startNode, [], set())
        return res