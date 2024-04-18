# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        arr=[]

        for key in count:
            arr.append((count[key]*-1, key))

        heapify(arr)
        res=[]

        for i in range(k):
            res.append(heappop(arr)[1])

        return res
        


        


        