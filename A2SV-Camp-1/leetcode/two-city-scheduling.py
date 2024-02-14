class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def custom(arr):
            return (arr[0]-arr[1])
        costs=sorted(costs, key=custom)
        cost=0
        # print(costs)
        for i in range(len(costs)):
            if i<len(costs)//2:
                cost+=costs[i][0]
            else:
                cost+=costs[i][1]

        return cost