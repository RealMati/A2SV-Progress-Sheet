class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minn=float('inf')
        l=0
        summ=0

        for r in range(len(nums)):
            summ+=nums[r]
            if summ>=target:
                minn=min(minn,r-l+1)
                while summ>=target:
                    summ-=nums[l]
                    l+=1
                minn=min(minn, r-l+2)

        if minn==float('inf'):
            return 0
        return minn



