class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        res=[]
        sum=0
        
        for num in nums:
            if num%2==0:
                sum+=num

        for val,idx in queries:
            initial=nums[idx]
            final=nums[idx]+val

            if initial%2==0 and final%2==1:
                sum-=initial
            elif initial%2==1 and final%2==0:
                sum+=final
                
            elif initial%2==0 and final%2==0:
                sum+=(final-initial)

            nums[idx]=final
            res.append(sum)
        return res
        