# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        last=nums[0]
        for i in range(1, len(nums)):
            last^=nums[i]
        return last