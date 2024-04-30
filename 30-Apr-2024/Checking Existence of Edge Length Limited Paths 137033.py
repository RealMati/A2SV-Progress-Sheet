# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        def union(a, b):
            parentA = find(a)
            parentB = find(b)
        
            parent[parentB] = parentA

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])

            return parent[x]

        for i in range(len(queries)):
            queries[i].append(i)

        visited=set()
        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])
        
        res=[False]*len(queries)
        
        parent = {i:i for i in range(n)}
        ptr=0
        for fromm ,to ,limit, idx in queries:

            if fromm not in parent or to not in parent: 
                continue

            # print(parent)
            while ptr < len(edgeList) and edgeList[ptr][-1] < limit:
                rootu = find(edgeList[ptr][0])
                rootv = find(edgeList[ptr][1])

                parent[rootu] = rootv
                ptr += 1

            if find(fromm)==find(to): res[idx]=True

        return res
      
