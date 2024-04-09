# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)

        def dfs(cur,parent):
            if cur:
                if parent:
                    graph[cur.val].append(parent.val)
                    graph[parent.val].append(cur.val)

                if cur.left:
                    dfs(cur.left,cur)
                if cur.right:
                    dfs(cur.right,cur)

        dfs(root,None)
        # print(graph)
        # return []
        visited=set([target.val])
        q=deque([target.val])
        
        while q and k:
            k-=1
            for i in range(len(q)):
                cur = q.popleft()

                for nbs in graph[cur]:
                    if nbs not in visited:
                        q.append(nbs)
                        visited.add(nbs)

        return list(q)
                
        
                