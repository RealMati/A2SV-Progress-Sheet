# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        # print(stones)
        while len(stones)>=2:
            y=heappop(stones)
            x=heappop(stones)
            res=y-x
            if res:
                heappush(stones, res)
        
        # print(stones)
        return stones[0]*-1 if stones else 0