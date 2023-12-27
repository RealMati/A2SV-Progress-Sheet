class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        count=set()



        for row in board:
            for col in row:
                if col!=".":
                    if col in count: return False
                    count.add(col)
            count=set()

        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col]!=".":
                    if board[row][col] in count: return False
                    count.add(board[row][col])
            count=set()

        for row in range(0,len(board),3):
            for col in range(0,len(board[0]),3):
                cells=[[row+1,col],[row+1,col+1],[row,col+1],[row+1,col+2],[row+2,col+1],[row+2,col+2],[row,col],[row+2,col],[row,col+2],]
                for y,x in cells:
                    if board[y][x]!=".":
                        if board[y][x] in count: return False
                        count.add(board[y][x])             
                count=set()
        
        return True

        

        

        
        