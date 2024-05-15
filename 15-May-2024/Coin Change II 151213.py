# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort()

        def dp(n, i):
            state = (n, i)

            if state in memo:
                return memo[state]

            if n == 0:
                return 1

            if i == len(coins) or n<0:
                return 0

            memo[state] = dp(n - coins[i], i) + dp(n, i + 1)

            return memo[state]

        return dp(amount, 0)
