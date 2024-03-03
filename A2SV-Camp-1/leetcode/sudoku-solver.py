class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(num, ro, co):
            for i in range(0, 9):
                if board[i][co] == num:
                    return False
                if board[ro][i] == num:
                    return False
                if board[3 * (ro // 3) + i // 3][3 * (co // 3) + i % 3] == num:
                    return False
            return True

        def c(row,col):
            if row == 9:
                return True
            if col==9: 
                return c(row+1,0)
            
                # print(row,col)
            if board[row][col] == ".":
                for num in range(1, 10):
                    v=valid(str(num), row, col)
                    print(row,col,v)
                    if v:
                        board[row][col] = str(num)
                        if c(row,col+1):
                            return True
                        board[row][col] = "."
                return False
            return c(row,col+1)

        c(0,0)
