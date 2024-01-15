class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        ct=left=0
        right=len(nums)-1

        while left<right:
            summ=nums[left]+nums[right]
            if summ==k:
                left+=1
                right-=1
                ct+=1
            elif summ>k:
                right-=1
            else:
                left+=1

        return ct
            

        