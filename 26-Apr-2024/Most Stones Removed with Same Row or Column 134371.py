# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent={}
        res=0
        rank={}
        column=defaultdict(list)
        row=defaultdict(list)
        
        for x,y in stones:
            parent[(x,y)]=(x,y)
            column[x].append((x,y))
            row[y].append((x,y))
            rank[(x,y)]=0

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
                    rank[parentA]+=1

        for key in column:
            for i in range(1, len(column[key])):
                union(column[key][i], column[key][i-1])

        for key in row:
            for i in range(1, len(row[key])):
                union(row[key][i], row[key][i-1])
                
        dic=defaultdict(int)
        for x,y in stones:
            dic[find((x,y))]+=1
        # print(dic)
        for key in dic:
            res+=(dic[key]-1)
        # print(parent)
        return res
            
                


