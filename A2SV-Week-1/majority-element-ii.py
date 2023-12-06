class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        import math
        target=math.floor(len(nums)/3)
        res=[]
        ct=0
        nums.sort()
        for i,num in enumerate(nums):
            if i==0 or (i>0 and num!=nums[i-1]):
                if ct>target: res.append(nums[i-1])
                ct=1
            else:
                ct+=1
        if ct>target: res.append(nums[-1])
        return res
        