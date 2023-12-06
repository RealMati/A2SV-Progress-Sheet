class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
            
        ct=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if i==0:
                    nums[i]=nums[i+1]
                else:
                    if nums[i+1]<nums[i-1]: nums[i+1]=nums[i]
                    else: nums[i]=nums[i+1]

                ct+=1
            if ct==2:
                return False
        return True