class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]

        def c(idx):
            if idx<=len(nums):
                res.append(ans[:])
                if ans and ans[-1]==nums[-1]: return 
                
            for i in range(idx,len(nums)):
                ans.append(nums[i])
                c(i+1)
                ans.pop()
        c(0)
        return res
