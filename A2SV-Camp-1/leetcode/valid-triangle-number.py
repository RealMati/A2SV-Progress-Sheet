class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        count = 0

        for third in range(2, len(nums)):
            first=0
            sec = third - 1
            while first< sec:
                if nums[first] + nums[sec] > nums[third]:
                    count += sec-first
                    # print(nums[first],nums[sec],nums[third])
                    sec -= 1
                else:
                    first += 1
        return count
