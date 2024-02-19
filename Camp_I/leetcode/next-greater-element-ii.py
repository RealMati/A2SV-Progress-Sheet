class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [i for i in range(len(nums))]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack.pop()] = nums[i]
        for i in range(len(stack)):
            ans[stack[i]] = -1
        return ans