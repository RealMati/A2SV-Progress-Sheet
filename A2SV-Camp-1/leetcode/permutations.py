class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        check=set()
        arr=[]
        def c(idx):
            if len(arr)==len(nums):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                if nums[i] in check: continue
                arr.append(nums[i])
                check.add(nums[i])
                c(i+1)
                arr.pop()
                check.remove(nums[i])
        c(0)
        return res