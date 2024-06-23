# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo = [[0] * len(dungeon[0]) for i in range(len(dungeon))]

        def fix(a,b,c):

            if a>0 and a>min(b,c):
                return 0
            else:
                return min(b,c)-a

        for col in range(len(dungeon[0]) - 1, -1, -1):
            for row in range(len(dungeon) - 1, -1, -1):
                if row == len(dungeon) - 1 and col == len(dungeon[0]) - 1:
                    memo[row][col] = fix(dungeon[row][col],0,0)
                elif row + 1 == len(dungeon):
                    memo[row][col] = fix(dungeon[row][col], memo[row][col + 1], float('inf'))
                elif col + 1 == len(dungeon[0]):
                    memo[row][col] = fix(dungeon[row][col], memo[row+1][col], float('inf'))
                else:
                    memo[row][col]=fix(dungeon[row][col], memo[row][col + 1], memo[row+1][col])
                    
        return abs(memo[0][0])+1
 
