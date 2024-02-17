class Solution:
    def triangleNumber(self, nums):
        n, total = len(nums), 0

        nums.sort()

        for i in range(2,n):
            low, high = 0, i-1 
            target = nums[i]

            while low < high:
                if nums[low] + nums[high] > target:
                    total += high - low 
                    high -= 1 
                else:
                    low += 1 

        return total


            
        