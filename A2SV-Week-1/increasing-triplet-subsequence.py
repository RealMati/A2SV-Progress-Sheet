class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1: return False 
        if len(nums)==2 : return False

        i=float('inf')
        j=float('inf')
        K=float('inf')
        for num in nums:
            if num<i:
                i=num
            elif i<num<j:
                j=num
            elif i<j<num:
                return True

        return False
        


            
        