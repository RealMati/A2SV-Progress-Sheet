# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}

        def dp(idx, buyState, ct):
            state=(idx, buyState,ct)

            if state in memo:
                return memo[state]

            if idx==len(prices) or ct==2:
                return 0

            if buyState:
                memo[state]=max(dp(idx+1, False, ct+1)+prices[idx], dp(idx+1, buyState,ct))
            else:
                memo[state]=max(dp(idx+1,True,ct)-prices[idx], dp(idx+1, buyState, ct))
            
            return memo[state]
            
        return dp(0,False, 0)