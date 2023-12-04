class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ct=0
        for point in range(len(points)-1):
            d1=points[point+1][0]-points[point][0]
            d2=points[point+1][1]-points[point][1]
            ct+=max(abs(d1),abs(d2))
        return ct