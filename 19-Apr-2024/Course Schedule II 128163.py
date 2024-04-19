# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        
        return res if len(res)==numCourses else []