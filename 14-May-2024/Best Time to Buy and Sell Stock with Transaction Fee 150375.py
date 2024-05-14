# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo={}

        def dp(idx, buyState):
            state=(idx, buyState)

            if state in memo:
                return memo[state]
            
            if idx==len(prices):
                return 0

            if buyState:
                memo[state]=max(dp(idx+1, False)+prices[idx], dp(idx+1, buyState))
            else:
                memo[state]=max(dp(idx+1, True)-prices[idx]-fee, dp(idx+1, buyState))

            return memo[state]
        
        return dp(0,False)
        