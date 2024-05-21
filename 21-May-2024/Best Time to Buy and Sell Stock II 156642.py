# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #hint: transitivity property
        # a-b +b-c + c-d = a-d
        res=0
        for i in range(len(prices)-1):
            res+=max(0, prices[i+1]-prices[i])
        return res
