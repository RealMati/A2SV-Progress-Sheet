# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float('inf')
        profit=0

        for num in prices:
            if num-minn>0:
                profit=max(profit, num-minn)
            else:
                minn=min(num, minn)
                
        return profit

        return 0