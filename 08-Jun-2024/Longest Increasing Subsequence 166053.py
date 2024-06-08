# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo={}
        res=0

        def dp(i):
            nonlocal res
            if i>=len(nums): return res
            if i in memo:
                return memo[i]

            maxx=0
            for j in range(i-1, -1, -1):
                if nums[j]<nums[i]:
                    maxx=max(maxx, memo[j])
            
            memo[i]=maxx+1
            res=max(res,memo[i])
            return dp(i+1)

        return dp(0)

                    
                

            