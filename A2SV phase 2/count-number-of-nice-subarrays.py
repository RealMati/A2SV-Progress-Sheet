class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]%2:
                nums[i]=1
            else:
                nums[i]=0
        summ=ct=0
        dic={0:1}
        for i in nums:
            summ+=i
            if summ-k in dic:
                ct+=dic[summ-k]
            if summ in dic:
                dic[summ]+=1
            else:
                dic[summ]=1
        return ct