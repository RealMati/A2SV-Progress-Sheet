# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()
        border=set()
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1:
                    if board[i][j]=="O":
                        q.append([i,j])
                        border.add((i,j))
                   

        while q:
            row,col=q.popleft()
            

            for dy,dx in dir:
                newCol=dx+col
                newRow=dy+row

                if (0<=newCol<len(board[0]) and 0<=newRow<len(board)) and (newRow,newCol) not in border and board[newRow][newCol]=='O':
                    q.append((newRow,newCol))
                    border.add((newRow,newCol))
        # print(border)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in border and board[i][j]=='O':
                    board[i][j]='X'