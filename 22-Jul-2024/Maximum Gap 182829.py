# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxx=p1=0
        p2=1

        while p2<len(nums):
            maxx=max(maxx, nums[p2]-nums[p1])
            p2+=1
            p1+=1

        return maxx