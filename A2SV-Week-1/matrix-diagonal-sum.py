class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        summ=mat[0][0]
        rows=len(mat)
        cols=len(mat[0])
        point=[0,0]
        while 0<=point[0]+1<rows and 0<= point[1]+1<cols:
            point[0]+=1
            point[1]+=1
            summ+=mat[point[0]][point[1]]
        point=[0,cols-1]
        summ+=mat[0][cols-1]
        while 0<=point[0]+1<rows and 0<= point[1]-1<cols:
            point[0]+=1
            point[1]-=1
            summ+=mat[point[0]][point[1]]
        if rows%2==1: summ-=mat[cols//2][rows//2]
        return summ