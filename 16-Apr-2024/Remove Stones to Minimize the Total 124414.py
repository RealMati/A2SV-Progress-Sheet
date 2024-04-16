# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        def heapup(cur):
    
            parent=(cur-1)//2

            if parent>=0 and heap[parent]<heap[cur]:
                heap[parent],heap[cur]=heap[cur],heap[parent]
                heapup(parent)

        def heapdown(parent):
            left=parent*2 +1
            right=parent*2 +2
            maxx=parent

            if left<len(heap) and heap[left]>heap[parent]:
                maxx=left
            if right<len(heap) and heap[right]>heap[maxx]:
                maxx=right

            if maxx!=parent:
                heap[parent],heap[maxx]=heap[maxx],heap[parent]
                heapdown(maxx)
        
        for val in piles:
            heap.append(val)
            cur=len(heap)-1
            heapup(cur)
            # print("pr",heap)
        # print("res",heap)


        
        for i in range(k):
            heap[0]=math.ceil(heap[0]/2)

            # heap[0],heap[len(heap)-1]=heap[len(heap)-1],heap[0]
            # print(heap)
            heapdown(0)
            # print('as',heap)

        return sum(heap)






# ;
#         def findMax(oiles):
#             maxx=0
#             for i in range(len(piles)):
#                 if piles[i]>piles[maxx]:
#                     maxx=i
#             return maxx
        
#         for i in range(k):
#             m=findMax(piles)
#             piles[m]= math.ceil(piles[m]/2)
#         # print(piles)
#         return sum(piles)
                