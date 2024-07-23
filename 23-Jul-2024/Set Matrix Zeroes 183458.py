# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #East
        for row in range(len(matrix)):
            found=False
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    found=True
                elif found:
                    matrix[row][col]=float('inf')
        
        #West
        for row in range(len(matrix)):
            found=False
            for col in range(len(matrix[0])-1,-1,-1):
                if matrix[row][col]==0:
                    found=True
                elif found:
                    matrix[row][col]=float('inf')

        #South
        for col in range(len(matrix[0])):
            found=False
            for row in range(len(matrix)):
                if matrix[row][col]==0:
                    found=True
                elif found:
                    matrix[row][col]=float('inf')

        #North
        for col in range(len(matrix[0])):
            found=False
            for row in range(len(matrix)-1, -1, -1):
                if matrix[row][col]==0:
                    found=True
                elif found:
                    matrix[row][col]=float('inf')

        #Clean up
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==float('inf'):
                    matrix[row][col]=0
                    
        return matrix
                