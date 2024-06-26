# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        sett=set(stones)
        last=stones[-1]
        memo={}

        def dp(place, jump):
            state=(place, jump)

            if state in memo:
                return memo[state]

            if place==last:
                return True
            if place not in sett:
                return False

            first= dp(place + jump-1, jump-1) if jump>1 else False
            
            memo[state]= first or dp(place+jump, jump) or dp(place+jump+1, jump+1)

            return memo[state]

        return dp(stones[1], 1) if stones[1]==1 else False
