class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        indices = []
        path = []
        visited=set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    indices.append([row, col])
            # east #west  # down  #up
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res=""

        def c(y, x, idx, path):
            nonlocal res
            if res==word: return res
            ans="".join(path)
            # print(ans)
            if  ans== word:
                res=ans
                return ans
            if (x,y) in visited:
                return 
            if not (0 <= y < len(board) and 0 <= x < len(board[0])):
                return
            if board[y][x] != word[idx]:
                return

            for dy, dx in dir:
                path.append(board[y][x])
                visited.add((x,y))
                c(y + dy, x + dx, idx + 1, path)
                path.pop()
                visited.remove((x,y))

            return res


        for y, x in indices:
            res = c(y, x, 0, [])
            if res == word:
                return True
        return False
