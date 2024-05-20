# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target=sum(nums)/k
        if target!=int(target): return False

        memo={}

        def dp(summ, mask):
            state=(summ, mask)

            if state in memo:
                return memo[state]
            
            if mask==2**len(nums)-1:
                if summ==target:
                    return True
                return False
            
            if summ==target:
                return dp(0,mask)
            
            res=False
            for i in range(len(nums)):
                if mask&1<<i: continue

                if nums[i]+summ<=target:
                    res=dp(summ+nums[i], mask|1<<i)
                    if res: break
            memo[state]=res
            return memo[state]
         
        return dp(0, 0)