# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx=max(nums)

        check=0
        for i in range(1, maxx+1):
            check^=i

        for i in nums:
            check^=i
        
        if check == 0 and 0 in nums:
            return maxx+1
        else:
            return check

