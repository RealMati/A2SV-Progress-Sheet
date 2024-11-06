class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        res=0

        for num in nums:
            if num-1 in sett:
                continue
            
            ans=0
            while num in sett:
                ans+=1
                num+=1
            
            res=max(res, ans)

        return res
