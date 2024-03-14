class Solution:
    def hIndex(self, nums: List[int]) -> int:
        l=res=0
        r=len(nums)-1
              
        while l<=r:
            mid=(l+r)//2

            if len(nums)-mid>=nums[mid]:
                res=max(nums[mid],res)
                l=mid+1
                
            else:
                res=max(len(nums)-mid, res)
                r=mid-1
                
        return res