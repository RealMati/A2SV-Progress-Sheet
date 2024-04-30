# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        parent = {}
        rank = {}
        maxx = {}

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]>0:
                    parent[(row, col)]=(row,col)
                    rank[(row, col)]=0
                    maxx[(row, col)]=grid[row][col]


        def union(a, b):
            parentA = find(a)
            parentB = find(b)
            rankA=rank[parentA]
            rankB=rank[parentB]

            if parentA!=parentB:
                if rankA>rankB:
                    parent[parentB] = parentA
                    maxx[parentA]+=maxx[parentB]
                elif rankA<rankB:
                    parent[parentA] = parentB
                    maxx[parentB]+=maxx[parentA]
                else:
                    parent[parentA] = parentB
                    maxx[parentB]+=maxx[parentA]
                    rank[parentB]+=1

        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]

            cur1 = x
            while cur1 != parent[cur1]:
                cur1=parent[cur1]

            return cur
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(r, c, start):
            # print(r,c, start)
            union((r,c), start)

            for dy,dx in dir:
                newCol=dx+c
                newRow=dy+r

                if (0<=newCol<len(grid[0]) and 0<=newRow<len(grid)) and (newRow,newCol) not in visited and grid[newRow][newCol]>0:
                    visited.add((newRow, newCol))
                    dfs(newRow, newCol, start)

        visited=set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col]>0:
                    visited.add((row,col))
                    dfs(row, col, (row, col))

        return max(maxx.values() if maxx else [0])
      
