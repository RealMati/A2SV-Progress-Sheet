class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # mini = float('inf')
        # for i in range(len(nums)-1):
        #     if nums[i]>mini:
        #         for j in range(i+1,len(nums)):
        #             if mini<nums[j]<nums[i]: #bruteforce
        #                 return True
        #     else:
        #         mini = nums[i]
        # return False
        stack = []
        sec = -float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<sec:
                return True
            while stack and stack[-1]<nums[i]:
                sec = stack.pop()
            stack.append(nums[i])
        return False
            