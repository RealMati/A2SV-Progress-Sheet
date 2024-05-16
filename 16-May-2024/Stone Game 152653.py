# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo={}

        def dp(left, right):
            state=(left, right)
            if state in memo:
                return memo[state]

            if left>right: return 0
            
            memo[state]=max(dp(left+1,right)+piles[left], dp(left,right-1)+piles[right])
            return memo[state]

        return (dp(0,len(piles)-1))>0