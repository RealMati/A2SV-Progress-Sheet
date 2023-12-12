class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            nums[i]=[num,i]
        nums=sorted(nums, key=lambda x:x[0])
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left][0]+nums[right][0]>target:
                right-=1
            elif nums[left][0]+nums[right][0]<target:
                left+=1
            else:
                return [nums[left][1],nums[right][1]]
  
