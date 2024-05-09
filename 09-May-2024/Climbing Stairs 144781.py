# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def dp(level):
            if level==1: return 1
            if level==2: return 2
            
            if level not in memo: 
                ans=dp(level-1)+dp(level-2)
                memo[level]=ans
            else:
                ans=memo[level]

            return ans
        
        return dp(n)