# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph=defaultdict(list)
        topo=defaultdict(list)

        for u,v in richer:
            graph[v].append(u)

        def dfs(node, r):
            topo[node].append((quiet[r], r))

            for nbs in graph[r]:
                if nbs not in visited:
                    dfs(node, nbs)
                    visited.add(nbs)
                     
        
        res=[]
        for i in range(len(quiet)):
            visited=set([i])
            dfs(i, i)
            res.append(min(topo[i])[1])

        return res