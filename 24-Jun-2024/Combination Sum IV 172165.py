# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={0:1}
        nums.sort()

        for i in range(1, target+1):
            memo[i]=0
            for num in nums:
                if num>i:
                    break
                memo[i]+=memo[i-num]

        return memo[target]

                
                
