# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def dp(idx,summ):
     
            if idx==len(nums):
                if summ==target:
                    return 1
                else:  return 0

            state=(idx,summ)

            if state not in memo:
                memo[state]= dp(idx+1, summ+nums[idx]) + dp(idx+1, summ-nums[idx])

            return memo[state]

        return dp(0,0)
