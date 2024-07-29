# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        non=0
        zer=0
        for i in nums:
            if i==0:
                non+=1
            else:
                nums[zer],nums[non]=nums[non],nums[zer]
                zer+=1
                non+=1
        return nums
        