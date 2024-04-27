# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree= [0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1

        q=deque([])
        for i in range(numCourses):
            if not indegree[i]: q.append(i)

        res=[]
        while q:
            node=q.popleft()
            res.append(node)

            for nbs in graph[node]:
                indegree[nbs]-=1
                if not indegree[nbs]:
                    q.append(nbs)
        
        return len(res)==numCourses