class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ct=0

        for idx,num in enumerate(nums):
            l=idx
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target:
                    ct+=(r-l)
                    break    
                r-=1

        return ct
