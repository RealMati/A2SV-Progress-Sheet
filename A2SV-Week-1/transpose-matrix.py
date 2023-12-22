class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        res=[]
        for col in range(len(matrix[0])):
            cell=[]
            for row in range(len(matrix)):

                cell.append(matrix[row][col])
            res.append(cell)
        
        return res