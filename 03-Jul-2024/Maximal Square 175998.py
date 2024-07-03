# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo=[[0]*len(matrix[0]) for p in range(len(matrix))]

        for row in range(len(matrix)-1,-1,-1):
            for col in range(len(matrix[0])-1, -1,-1):
                if matrix[row][col]=="1":
                    right= memo[row][col+1] if col+1<len(matrix[0]) else 0
                    down= memo[row+1][col] if row+1<len(matrix) else 0
                    diagonal=memo[row+1][col+1] if row+1<len(matrix) and col+1<len(matrix[0]) else 0

                    memo[row][col]=1+min(right, down, diagonal)

                else:
                    memo[row][col]=0

        res=0
        for row in range(len(matrix)-1,-1,-1):
            for col in range(len(matrix[0])-1, -1,-1):
                res=max(res, memo[row][col])
        # print(memo)
        return res**2


