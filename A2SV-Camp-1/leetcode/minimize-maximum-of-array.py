class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx = nums[0]
        excess = 0
        summ = nums[0]

        for i in range(1, len(nums)):
            summ += nums[i]
            
            if nums[i] - maxx > excess:
                nums[i] -= excess
                maxx += ceil((nums[i] - maxx) / (i + 1))

            excess = maxx * (i + 1) - summ

        return maxx
                