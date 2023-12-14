class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0   
        nums=set(nums)
        nums=sorted(nums)
        maxct=ct=0

        for i in range(1,len(nums)):

            if nums[i]-nums[i-1]==1:
                ct+=1
            else:
                maxct=max(maxct,ct)
                ct=0
        maxct=max(maxct,ct)
        return maxct+1