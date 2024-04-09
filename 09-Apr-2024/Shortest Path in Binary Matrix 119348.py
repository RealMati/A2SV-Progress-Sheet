# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        visited = set()
        q = deque()
        q.append((0, 0))
        if grid[0][0] == 1:
            return -1
        moves = 0

        while q:
            # print(q)
            moves += 1
            for i in range(len(q)):
                row, col = q.popleft()
                if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                    return moves

                for dx, dy in dir:
                    newRow = row + dy
                    newCol = col + dx

                    if (
                        0 <= newRow < len(grid)
                        and 0 <= newCol < len(grid[0])
                        and grid[newRow][newCol]==0 and (newRow,newCol) not in visited
                    ):
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
        return -1
