# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent={}
        graph=defaultdict(list)
        res=0
        edges=[]
        rank={}
        
        for x,y in points:
            parent[(x,y)]=(x,y)
            rank[(x,y)]=0

        for i in range(len(points)):
            x,y=points[i]
            for j in range(len(points)):
                if i!=j:
                    x1,y1=points[j]
                    d=abs(x-x1) + abs(y-y1)
                    edges.append([d,(x1,y1),(x,y)])

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

            if rankA>rankB:
                parent[parentB] = parentA
            elif rankA<rankB:
                parent[parentA] = parentB
            else:
                parent[parentA] = parentB
                rank[parentA]+=1


        edges.sort()
        treeNo=0

        for w, v1, v2 in edges:
                if find(v1)!=find(v2):
                    union(v1,v2)
                    res+=w
                    treeNo+=1
                if treeNo==len(points)-1:
                    return res

        return res
            
                


