# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo={}

        def dp(row,col):
            state=(row,col)

            if state in memo:
                return memo[state]
            if row==len(obstacleGrid) or col==len(obstacleGrid[0]) or obstacleGrid[row][col]:
                return 0
            if row==len(obstacleGrid)-1 and col==len(obstacleGrid[0])-1:
                return 1

            memo[state]= dp(row+1, col)+dp(row,col+1)

            return memo[state]
            
        return dp(0,0)