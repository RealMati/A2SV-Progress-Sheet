class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ct=0

  
        for index in range(len(nums)):
            for idx in range(index+1,len(nums)):
                if nums[index]==nums[idx]:
                    if (index*idx)%k==0:
                        ct+=1
            
        return ct
