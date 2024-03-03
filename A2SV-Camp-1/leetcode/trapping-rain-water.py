class Solution:
    def trap(self, nums: List[int]) -> int:
        stack = []
        i, res = 0, 0

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                last = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                res += distance * (min(nums[i], nums[stack[-1]]) - nums[last])
            
            stack.append(i)

        return res