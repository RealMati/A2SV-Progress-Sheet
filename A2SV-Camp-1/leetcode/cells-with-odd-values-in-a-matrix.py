class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        grid=[[0]*n for  _ in range(m)]
        res=0

        def go(row,col):
            for c in range(n):
                grid[row][c]+=1
            for r in range(m):
                grid[r][col]+=1

        for row,col in indices:
            go(row,col)

        for row in range(m):
            for col in range(n):
                if grid[row][col]%2:
                    res+=1

        return res