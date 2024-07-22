# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=3: return 0
        minn=float('inf')
        r=len(nums)-3
        l=0

        while r<=len(nums):
            minn=min(minn, nums[r-1]-nums[l])
            r+=1
            l+=1

        return minn


        