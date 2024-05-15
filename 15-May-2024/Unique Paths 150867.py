# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(row, col):
            state = (row, col)

            if state in memo:
                return memo[state]

            if row == m-1 or col == n-1:
                return 1
            if row==m or col==n:
                return 0
            
            memo[state]=dp(row+1,col)+dp(row,col+1)
            

            return memo[state]

        return dp(0, 0)
