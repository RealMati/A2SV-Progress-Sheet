class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            mid=(l+r)//2
            print(mid,l,r)
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==len(nums)-1 or nums[mid]<nums[mid+1]):
                l=mid+1
            else:
                r=mid-1
        
        return l