class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ct=len(nums)
        for idx,num in enumerate(nums):
            if num==val:
                nums[idx]='_'
                ct-=1

        read=write=0

        while read<len(nums):
            if nums[read]!='_':
                nums[read],nums[write]=nums[write],nums[read]
                read+=1
                write+=1
            else:
                read+=1
        
        return ct