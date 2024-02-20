class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        res=idx=0
        q=deque()

        while nums[k]!=0:
            if nums[idx]: 
                nums[idx]-=1
                res+=1
            idx=(idx+1)%len(nums)
            
        return res