# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dp(n):
            state = (n)

            if state in memo:
                return memo[state]

            if n == 2 or n==1:
                return 1    

            memo[state]=max(max(a,dp(a))*max(n-a,dp(n-a)) for a in range(1,math.ceil((n+1)/2)))

            return memo[state]

        return dp(n)
