class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maximum_sum=0

        for i in range(len(nums)-2):
            side_sum = nums[i]+nums[i+1]
            larger_side=nums[i+2]
            tot_sum=side_sum+larger_side
            if side_sum>larger_side:
                maximum_sum=max(maximum_sum,tot_sum)
        
        return maximum_sum