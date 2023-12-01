class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for vert in range(1,len(matrix)):
            for hor in range(1,len(matrix[0])):
                if matrix[vert][hor]!=matrix[vert-1][hor-1]:
                    return False
        return True


                    

        