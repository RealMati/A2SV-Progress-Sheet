class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        right=nums.count(1)
        left=0
        maxPair=[right,[0]]

        for idx,bit in enumerate(nums):
            if bit:
                right-=1
                if left+right>maxPair[0]:
                    maxPair=[left+right,[idx+1]]
                elif left+right==maxPair[0]:
                    maxPair[1].append(idx+1)
            else:
                left+=1
                if left+right>maxPair[0]:
                    maxPair=[left+right,[idx+1]]
                elif left+right==maxPair[0]:
                    maxPair[1].append(idx+1)
        return maxPair[1]

