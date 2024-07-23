# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[0 for i in range(n)]

        def find(x):
            cur=cur2=x
            while cur!=parent[cur]:
                cur=parent[cur]
            
            while cur2!=cur:
                next=parent[cur2]
                parent[cur2]=cur
                cur2=next

            return cur                

        def union(a,b):
            parentA=find(a)
            parentB=find(b)
            rankA=rank[a]
            rankB=rank[b]

            if rankA>rankB:
                parent[parentB]=parentA
                rankA+=rankB
            else:
                parent[parentA]=parentB
                rankB+=rankA
            
        for x,y in edges:
            union(x,y)
        
        dic=defaultdict(int)
        for i in range(n):
            dic[find(i)]+=1
        
        res=0
        for val in dic.values():
            res+=(n-val)*val

        return res//2