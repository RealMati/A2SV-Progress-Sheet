# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def check(idx):
            if nums[0]>nums[idx]:
                return True
            else:
                return False

        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                l=mid
                break
            if check(mid):
                r=mid-1
            else:
                l=mid+1
        # print(l)
        def binsearch(l,r):
            while l<=r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l=mid + 1
                else:
                    r=mid - 1   
                # print(mid)
            return -1
        
        a=binsearch(0,l-1)
        b=binsearch(l,len(nums)-1)
        # print(a,b)
        return a if a!=-1 else b