class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        arr=[]
        def c(idx):
            if idx<=len(nums):
                res.add(tuple(arr[:]))
                if idx==len(nums): return 

            for i in range(idx,len(nums)):
                arr.append(nums[i])
                c(i+1)
                arr.pop()
        c(0)
        return res