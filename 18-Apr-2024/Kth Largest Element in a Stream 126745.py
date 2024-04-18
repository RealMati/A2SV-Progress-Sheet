# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        # for i in range(len(nums)):
        #     nums[i]*=-1

        self.heap=[]
        heapq.heapify(self.heap)
                
        for i in range(len(nums)):
            if i<self.k:
                heappush(self.heap, nums[i])
            else:
                # print(self.heap, self.heap[-1])
                if self.heap[0]<nums[i]:
                    heapreplace(self.heap, nums[i])
        
        # print(self.heap)

    def add(self, val: int) -> int:
        if self.heap and self.heap[0]<val and len(self.heap)==self.k:
            heapreplace(self.heap, val)

        if not self.heap or len(self.heap)<self.k:
            heappush(self.heap, val)

        return self.heap[0] if len(self.heap)==self.k else 0
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)