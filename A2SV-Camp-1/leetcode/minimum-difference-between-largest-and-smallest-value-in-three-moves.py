class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums)<=3: return 0
        res=float('inf')

        for r in range(len(nums)-4,len(nums)):
            res=min(res,(nums[r]-nums[r-len(nums)+4]))

        return res
                
            