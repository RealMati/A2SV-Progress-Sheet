# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for i in range(len(arr)):
            arr[i]=(abs(arr[i]-x), arr[i])
        # print(arr)
        heapify(arr)
        res=[]

        for i in range(k):
            res.append(heappop(arr)[1])

        return sorted(res)
        


        


        