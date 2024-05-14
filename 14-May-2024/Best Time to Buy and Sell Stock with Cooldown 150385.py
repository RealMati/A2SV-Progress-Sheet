# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}

        def dp(idx, buyState, cooldown):
            state= (idx, buyState, cooldown)
            if state in memo:
                return memo[state]

            if idx==len(prices):
                return 0
            
            if cooldown:
                memo[state]=dp(idx+1, False, False)
            elif buyState:
                memo[state]=max(dp(idx+1, False, True)+prices[idx], dp(idx+1, buyState,cooldown))
            else:
                memo[state]=max(dp(idx+1, True, cooldown)-prices[idx], dp(idx+1, buyState,cooldown))

            return memo[state]
            
                
        return  dp(0,False,False)