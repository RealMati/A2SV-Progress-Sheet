class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        nums.sort(reverse=True)
        for start, end in req:
            prefix[start + 1] += 1
            if end+2<len(prefix): prefix[end + 2] -= 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        print(prefix)
        order = sorted(list(enumerate(prefix[1:])), key=lambda x: x[1], reverse=True)
        arr = [0]
        arr.extend(nums[:])

        for i in range(len(nums)):
            arr[order[i][0]+1] = nums[i]
        # print(arr)

        for i in range(1, len((arr))):
            arr[i] += arr[i - 1]
        # print(arr)
        summ = 0

        for start, end in req:
            summ += arr[end+1] - arr[start]

        # print(arr)
        return summ % (10**9 + 7)
