# Problem: Minimum Height Trees  - https://leetcode.com/problems/minimum-height-trees/description/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        incoming=defaultdict(int)
        vertices=set(i for i in range(n))

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            incoming[u]+=1
            incoming[v]+=1

        q=deque()
        for node in incoming:
            if incoming[node]==1:
                q.append(node)
        
        while q and len(vertices)>2:
            for i in range(len(q)):
                cur=q.popleft()
                incoming[cur]-=1
                vertices.remove(cur)

                for nbs in graph[cur]:
                    incoming[nbs]-=1
                    if incoming[nbs]==1:
                        q.append(nbs) 

        return list(vertices)

