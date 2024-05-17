# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo={(len(matrix)-1, col): matrix[len(matrix)-1][col] for col in range(len(matrix[0]))}

        dir=[(1, -1), (1, 0), (1, 1)]
        for row in range(len(matrix)-2,-1,-1):
            for col in range(len(matrix)):
                state=(row,col)
                minn=float('inf')
                for dy,dx in dir:
                    newRow=dy+row
                    newCol=dx+col
                    if 0<=newRow<len(matrix) and 0<=newCol<len(matrix[0]):
                        minn=min(minn, memo[(newRow,newCol)])

                memo[state]=minn+matrix[row][col]

        minn=float('inf')
        for col in range(len(matrix[0])):
            minn=min(minn, memo[(0, col)])
        
        return minn
        

