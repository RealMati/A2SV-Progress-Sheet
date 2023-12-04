class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=curmax=0
        for i in nums:
            if i:
                curmax+=1
            else:
                maxx=max(curmax,maxx)
                curmax=0
        
        return max(curmax,maxx)
        