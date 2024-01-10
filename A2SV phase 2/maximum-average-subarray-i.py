class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        for idx in range(0,k):
            summ+=nums[idx]
        maxSum=summ
        print(maxSum)
        for idx in range(k,len(nums)):
            summ-=nums[idx-k]
            summ+=nums[idx]
            maxSum=max(maxSum,summ)
            # print(idx, summ)
            
        return maxSum/k