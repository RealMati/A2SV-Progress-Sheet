class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
        def validPos(ro,co):
            # for rr in range(n):
            #     if board[rr][col]=="Q":
            #         return 
            row,col=ro,co
            for cc in range(col):
                if board[row][cc]=="Q":
                    return False

            #North West
            row,col=ro,co
            while row-1>=0 and col-1>=0:
                if board[row-1][col-1]=="Q":
                    return False
                row-=1
                col-=1

            #NOrth East
            # while row-1>=0 and col+1<n:
            #     if board[row-1][col+1]=="Q":
            #         return False
            #     row-=1
            #     col+=1

            #South West
            row,col=ro,co
            while row+1<n and col-1>=0:
                if board[row+1][col-1]=="Q":
                    return False
                row+=1
                col-=1
            
            #South East
            # while row+1<n and col+1<n:
            #     if board[row+1][col+1]=="Q":
            #         return False
            #     row+=1
            #     col+=1
            return True            

        def c(col):         
            if col==n:
                res.append(["".join(i) for i in board])
                return 
                
            for row in range(n):
                if validPos(row,col):
                    board[row][col]='Q'
                    c(col+1)
                    board[row][col]="."

        if 2<=n<=3: return []
        c(0)
        return res