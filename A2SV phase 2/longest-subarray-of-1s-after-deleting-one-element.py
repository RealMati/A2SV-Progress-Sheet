class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
 
        l=0
        r=0
        dic=set()
        maxx=0

        for r in range(len(nums)):
            if nums[r]==1:
                continue
            if nums[r]==0 and nums[r] not in dic:
                dic.add(0)
            else:
                maxx=max(maxx,r-l-1)
                while nums[l]!=0:
                    l+=1
                l+=1

        maxx=max(maxx,r-l)

        return maxx
                    
            



            

