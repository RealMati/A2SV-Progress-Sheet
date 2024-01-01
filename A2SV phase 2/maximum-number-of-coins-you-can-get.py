class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        summ=0

        for idx in range(len(piles)-2,len(piles)//3-1,-2):
            summ+=piles[idx]
        
        return summ