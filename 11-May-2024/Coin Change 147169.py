# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo={}
        maxx=float('inf')

        def dp(summ, cur):
            nonlocal maxx
            if summ == amount:
                maxx = min(maxx, len(cur))
                return 

            if summ > amount:
                return

            if summ in memo and memo[summ] <= len(cur):
                return

            memo[summ] = len(cur)
            for coin in coins:
                dp(summ + coin, cur + [coin])

        dp(0,[])
        return maxx if maxx != float('inf') else -1


            





