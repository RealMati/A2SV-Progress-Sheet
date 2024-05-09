# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        lastCur=last=0
        
        for i in range(len(nums)):
            summ=nums[i]+lastCur
            lastCur=last
            last=max(last, summ)
            
        return last
        

