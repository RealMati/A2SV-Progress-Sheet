# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        arr=[]

        for key in count:
            arr.append((count[key]*-1, key))

        heapify(arr)
        res=[]

        for i in range(k):
            res.append(heappop(arr)[1])

        return res
        


        


        