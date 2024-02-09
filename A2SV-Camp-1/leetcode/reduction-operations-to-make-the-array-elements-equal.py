class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        unique=sorted(list(set(nums)))
        dic={}
        res=0
        
        for idx,num in enumerate(nums):
            if num not in dic:
                dic[num]=idx

        for idx in range(len(unique)-1,0,-1):
            res+=(len(nums)-dic[unique[idx]])
        
        return res