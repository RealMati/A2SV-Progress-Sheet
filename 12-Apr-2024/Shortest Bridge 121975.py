# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        flag=False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    explore=(i,j)
                    flag=True
                    break
            if flag: break

        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        borders=[]
        b=deque([explore])
        visited=set()
        visited.add(explore)
        while b:
            # print(b.popleft())
            row,col=b.popleft()
            for dy,dx in dir:
                newCol=dx+col
                newRow=dy+row

                if (0<=newCol<len(grid[0]) and 0<=newRow<len(grid)) and (row,col,0) not in borders and grid[newRow][newCol]==0:
                    borders.append((row,col,0))

                elif (0<=newCol<len(grid[0]) and 0<=newRow<len(grid)) and (newRow,newCol) not in visited and grid[newRow][newCol]==1:    
                    b.append((newRow,newCol))
                    visited.add((newRow,newCol))

        q=deque(borders)

        # print(q)
        while q:
            # print(q)
            row,col,level=q.popleft()

            for dy,dx in dir:
                newCol=dx+col
                newRow=dy+row

                if (0<=newCol<len(grid[0]) and 0<=newRow<len(grid)) and (newRow,newCol) not in visited:
                    if grid[newRow][newCol]==1:
                        return level
                    q.append((newRow,newCol,level+1))
                    visited.add((newRow,newCol))


