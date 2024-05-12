# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo={}
        minn=float('inf')

        def dp(amount):
            global minn

            state=(amount)
            if state in memo:
                return memo[state]

            if amount==0:
                return 0
            ans=float('inf')
            for coin in coins:
                if coin<=amount:
                    ans=min(ans ,dp(amount-coin)+1)
                else:
                    break
            memo[state]=ans
            return memo[state]

        res=dp(amount) 
        return res if res!=float('inf') else -1