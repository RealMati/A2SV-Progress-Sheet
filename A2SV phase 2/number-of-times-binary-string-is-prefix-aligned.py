class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        maxNum=0
        ct=0

        for idx,num in enumerate(flips):
            maxNum=max(maxNum,num)
            if num<=idx+1:
                if maxNum==idx+1:
                    ct+=1
        
        return ct