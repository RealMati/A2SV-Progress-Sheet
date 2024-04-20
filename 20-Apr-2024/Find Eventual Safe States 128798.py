# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        q=deque()
        outdegree=[]
        res=[]
        for idx,arr in enumerate(graph):
            outdegree.append(len(arr))
            if len(arr)==0:
                q.append(idx)
                res.append(idx)

        dic=defaultdict(list)
        for i in range(len(graph)):
            for nb in graph[i]:
                dic[nb].append(i)

        while q:
            cur=q.popleft()

            for nbs in dic[cur]:
                outdegree[nbs]-=1
                if not outdegree[nbs]:
                    q.append(nbs)
                    res.append(nbs)
                    
        return sorted(res)



