class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        nums.extend(nums)
        res=[-1]*(len(nums)+1)
        for idx,num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                res[stack[-1]]=num
                stack.pop()
            stack.append(idx)
        
        res.pop()
        return res[:len(nums)//2]