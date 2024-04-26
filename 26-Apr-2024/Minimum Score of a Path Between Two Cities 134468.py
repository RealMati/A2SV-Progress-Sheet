# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent={i:i for i in range(1,n+1)}
        res=0
        rank={i:0 for i in range(1,n+1)}
        column=defaultdict(list)
        minn={i:float('inf' ) for i in range(1,n+1)}

        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]

            cur1=x
            while cur1!=parent[cur1]:
                parent[cur1]=cur
                cur1=parent[cur1]
            
            return cur

        def union(a, b):
            parentA = find(a)
            parentB = find(b)
            rankA=rank[parentA]
            rankB=rank[parentB]

            if parentA!=parentB:
                if rankA>rankB:
                    parent[parentB] = parentA
                elif rankA<rankB:
                    parent[parentA] = parentB
                else:
                    parent[parentA] = parentB
                    rank[parentB]+=1
        
        for u,v,w in roads:
            minn[u]=min(minn[u],w)
            minn[v]=min(minn[v],w)

            union(u,v)
        
        # print(parent)
        p=find(1)
        res=float('inf')
        for key in parent:
            if find(key)==p:
                res=min(res, minn[key])
        return res
            
                


