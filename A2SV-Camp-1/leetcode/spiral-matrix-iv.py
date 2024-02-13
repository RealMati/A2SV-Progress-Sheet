# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for i in range(m)]
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = 0, 0
        cur = head
        d = 0

        while cur:
            grid[y][x] = cur.val
            cur = cur.next
            # print(x,y)
            if not (
                0 <= (x + dir[d][0]) < n
                and 0 <= (y + dir[d][1]) < m
                and grid[y + dir[d][1]][x + dir[d][0]] == -1
            ):
                d = (d+1)%4 

            x += dir[d][0]
            y += dir[d][1]

        return grid
