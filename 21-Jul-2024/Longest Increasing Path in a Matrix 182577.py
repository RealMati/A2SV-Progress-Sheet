# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo={}
        def dfs(row, col):
            state=(row,col)
            if state in memo:
                return memo[state]

            maxx=0
            for xd, yd in dir:
                newRow = yd + row
                newCol = xd + col
                newstate=(newRow,newCol)

                if (
                    0 <= newRow < len(matrix)
                    and 0 <= newCol < len(matrix[0])
                ):
                    if matrix[row][col] < matrix[newRow][newCol]:
                        # visited.add((newRow, newCol))
                        maxx=max(maxx, dfs(newRow, newCol)+1)
            
            memo[state]=maxx
            return maxx

        res=0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res=max(res, dfs(row, col))
       
        # print(memo)
        return res+1