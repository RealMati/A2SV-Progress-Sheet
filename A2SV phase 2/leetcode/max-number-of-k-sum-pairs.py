class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l=ct=0
        r=len(nums)-1
    
        while l<r:
            summ=nums[l]+nums[r]
            if summ==k:
                ct+=1
                l+=1
                r-=1
            elif summ>k:
                r-=1
            else:
                l+=1

        return ct
            

        