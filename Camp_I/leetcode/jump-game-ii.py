class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0
        n = len(nums)
        while i<n-1:
            currmax = 0
            idx = 0
            for j in range(nums[i],-1,-1):
                if i<n and nums[i]-j>currmax:
                    currmax = nums[i]-j
                    idx = i
                if i==n-1:
                    idx = i
                    break
                i+=1
            count+=1
            i=idx
        return count
            
