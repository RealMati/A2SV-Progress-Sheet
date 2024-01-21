class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minn=float('inf')
        for i in range(len(nums)):
            l=0
            r=len(nums)-1

            while l<r:
                if l==i:
                    l+=1
                    continue
                elif r==i:
                    r-=1
                    continue 
                summ=nums[l]+nums[r]+nums[i]
                if abs(target-summ) < abs(target-minn):
                    minn=summ
                if summ==target:
                    return target
                    break       
                elif summ<target:
                    l+=1
                else:
                    r-=1
       
        return minn
            