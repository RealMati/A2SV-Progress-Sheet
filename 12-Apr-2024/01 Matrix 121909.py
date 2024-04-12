# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        visited=set()
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    visited.add((i,j))
                else:
                    mat[i][j]=float('inf')

        while q:
            row,col,level=q.popleft()
            if mat[row][col]==float('inf'):
                mat[row][col]=min(level, mat[row][col])

            for dy,dx in dir:
                newCol=dx+col
                newRow=dy+row

                if (0<=newCol<len(mat[0]) and 0<=newRow<len(mat)) and (newRow,newCol) not in visited and mat[newRow][newCol]==float('inf'):
                    q.append((newRow,newCol,level+1))
                    visited.add((newRow,newCol))
    
        return mat
