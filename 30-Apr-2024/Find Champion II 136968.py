# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        incoming=defaultdict(int)

        for u,v in edges:
            graph[u].append(v)
            incoming[v]+=1

        
        q=deque()
        for i in range(n):
            if not incoming[i]:
                q.append(i)
                
        
       
        return q.popleft() if len(q)==1 else -1
            
                            



