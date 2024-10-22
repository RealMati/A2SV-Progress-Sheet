import heapq
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid) 
        n = len(grid[0]) 

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap=[(0,0,0,k)]
        heapq.heapify(heap)
        processed=set()

        while heap:
            move, row, col, k = heappop(heap)
            if k<0: continue
            if (col, row)==(n-1, m-1):
                return move

            if (row, col, k) in processed: continue
            processed.add((row, col, k))
            
            for dy, dx in dir:
                newRow=row+dy
                newCol=col+dx

                if 0<=newRow<len(grid) and 0<=newCol<len(grid[0]):
                    state = (move+1,newRow,newCol,k-1) if grid[newRow][newCol]==1 else (move+1,newRow,newCol,k)
                    heapq.heappush(heap, state)

        return -1



