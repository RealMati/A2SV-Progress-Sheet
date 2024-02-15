class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def comparator(arr):
            return arr[1]
        points=sorted(points,key=comparator)
        arrows=0

        for p in range(1,len(points)):
            if points[p][0]<=points[p-1][1]:
                points[p][1]=points[p-1][1]
            else:
                arrows+=1

        return arrows+1