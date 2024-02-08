class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        res=[]
        nums.sort()

        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])

        for idx,num in enumerate(nums):
            if idx-1>=0:
                left=abs(prefix[idx-1]-(idx*num))
            else:
                left=0

            right=abs((prefix[-1]-prefix[idx])-(len(nums)-idx-1)*num)
            res.append(left+right)
        
        return res