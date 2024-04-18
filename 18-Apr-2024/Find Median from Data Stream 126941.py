# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.minn=[]
        self.maxx=[]
        heapq.heapify(self.minn)
        heapq.heapify(self.maxx)

    def addNum(self, num: int) -> None:
        if len(self.minn)==len(self.maxx):
            if self.minn and self.minn[0]<num:
                top=heappop(self.minn)
                heappush(self.minn, num)
                heappush(self.maxx, top*-1)
            else:
                heappush(self.maxx, num*-1)

        elif len(self.minn)+1==len(self.maxx):
            if self.maxx[0]*-1>num:
                top=heappop(self.maxx)*-1
                heappush(self.minn, top)
                heappush(self.maxx, num*-1)
            else:
                heappush(self.minn, num)
        # print(num,self.maxx, self.minn)
    def findMedian(self) -> float:
        if len(self.minn)==len(self.maxx):
            return (self.minn[0]+self.maxx[0]*-1)/2
        else:
            return self.maxx[0]*-1


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()