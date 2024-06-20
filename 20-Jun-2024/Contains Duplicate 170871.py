# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False