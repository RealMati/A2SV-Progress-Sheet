class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        maxBars=0
        idx=0
        while coins>0 and idx<len(costs):
            if costs[idx]<=coins:
                maxBars+=1
                coins-=costs[idx]
            else:
                break
            idx+=1

        return maxBars


        