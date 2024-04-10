# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def check(mid,r):
            return nums[mid]<=nums[r]
        l=0
        r=len(nums)-1

        while l<r:
            mid=(l+r)//2
            if check(mid,r):
                r=mid
            else:
                l=mid+1
            
        return nums[l]