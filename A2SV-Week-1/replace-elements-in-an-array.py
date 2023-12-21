class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        idxpool={}

        for idx,num in enumerate(nums):

            idxpool[num]=idx

        for initial,final in operations:

            nums[idxpool[initial]]=final

            idxpool[final]=idxpool[initial]
            del idxpool[initial]

        return nums
        