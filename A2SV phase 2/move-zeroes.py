class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
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