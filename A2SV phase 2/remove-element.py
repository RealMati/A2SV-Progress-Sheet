class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        read=write=0

        while read<len(nums):
            if nums[read]!=val:
                nums[read],nums[write]=nums[write],nums[read]
                read+=1
                write+=1
            else:
                read+=1
        
        return write