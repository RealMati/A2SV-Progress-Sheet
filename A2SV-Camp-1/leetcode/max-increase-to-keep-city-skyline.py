class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax=[]
        colMax=[]
        size=len(grid)

        for i in range(size):
            maxx=0
            for j in range(size):
                maxx=max(grid[j][i],maxx)
            colMax.append(maxx)
            
        for i in range(size):
            maxx=0
            for j in range(size):
                maxx=max(grid[i][j],maxx)
            rowMax.append(maxx)
        # print(colMax,rowMax)
        res=0
        for i in range(size):
            for j in range(size):
                res+=(min(colMax[j],rowMax[i])-grid[i][j])

        # print(grid)
        return res
        

        
        