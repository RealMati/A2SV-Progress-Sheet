class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        for i in range(len(nums)):
            ct=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    ct+=1
            if ct!=0:
                res[i]=ct
        return res