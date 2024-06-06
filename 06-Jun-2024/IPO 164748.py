# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        for i in range(len(profits)):
            capital[i]=[capital[i], profits[i]]
        
        capital.sort()
        heap=[]
        heapify(heap)
        idx=0

        while k:
            while idx<len(profits):
                if capital[idx][0]<=w:
                    heappush(heap,-1*capital[idx][1])
                    idx+=1
                else:
                    break

            if heap: w+=abs(heappop(heap))
            k-=1

        return w
                
            



             