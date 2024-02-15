class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        check = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= check:
                check = nums[i]
                continue

            buckets = math.ceil(nums[i] / check)
            check = nums[i] // (buckets)
            res += buckets - 1

        return res
