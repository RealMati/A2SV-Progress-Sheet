# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j,0])
                    visited.add((i,j))

        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        global level

        while q:
            row,col,level=q.popleft()
            
            for dy,dx in dir:
                newCol=dx+col
                newRow=dy+row

                if (0<=newCol<len(grid[0]) and 0<=newRow<len(grid)) and grid[newRow][newCol]==1 and (newRow,newCol) not in visited:
                    q.append((newRow,newCol,level+1))
                   
                    grid[newRow][newCol]=2
                    visited.add((newRow,newCol))
            
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return level
