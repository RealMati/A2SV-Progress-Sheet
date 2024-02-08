class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        suffix=sum(nums)
        prefix=0

        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix==suffix:
                return i

            suffix-=nums[i]
        
        return -1