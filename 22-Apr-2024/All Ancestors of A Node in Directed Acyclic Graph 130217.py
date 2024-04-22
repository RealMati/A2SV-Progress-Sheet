# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        indegree=defaultdict(int)

        for u,v in edges:
            graph[v].append(u)
        
        for k in graph:
            graph[k]=sorted(graph[k])
        print(graph)
        
        def dfs(node, start):
            for nbs in graph[node]:
                if nbs not in visited:
                    visited.add(nbs)
                    ancestor[start].add(nbs)
                    dfs(nbs,start)

        ancestor=defaultdict(set)
        res=[]
        for i in range(n):
            visited=set([i])
            dfs(i, i)
            res.append(sorted(list(ancestor[i])))
        # print(ancestor)
        return res