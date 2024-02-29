class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack=[]
        popped=float('-inf')

        for i in range(len(nums)-1,-1,-1):
            if stack and stack[-1]>nums[i] and popped>nums[i]:
                return True
            while stack and stack[-1]<nums[i]:
                popped=stack[-1]
                stack.pop()
            print(popped,nums[i],i)
            stack.append(nums[i])
        print(stack, popped)
        return False
