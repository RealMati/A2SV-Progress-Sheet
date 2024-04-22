# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        indegree=defaultdict(int)

        for u,v in prerequisites:
            graph[v].append(u)
        
        for k in graph:
            graph[k]=sorted(graph[k])
        # print(graph)
        
        def dfs(node, start):
            for nbs in graph[node]:
                if nbs not in visited:
                    visited.add(nbs)
                    ancestor[start].add(nbs)
                    dfs(nbs,start)

        ancestor=defaultdict(set)
        res=[]
        for i in range(numCourses):
            visited=set([i])
            dfs(i, i)
        # print(ancestor)
        for u,v in queries:
            res.append(u in ancestor[v])

        return res