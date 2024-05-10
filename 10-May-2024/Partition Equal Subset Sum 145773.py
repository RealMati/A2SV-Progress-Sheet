# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        summ=sum(nums)
        nums.sort()

        if summ%2: return False
        target=summ//2

        def dp(idx, target):
            if idx==len(nums):
                return target==0
            
            state=(idx,target)
            if state not in memo:
                memo[state]= dp(idx+1, target-nums[idx]) or dp(idx+1, target)
            
            return memo[state]
        
        return dp(0, target)
