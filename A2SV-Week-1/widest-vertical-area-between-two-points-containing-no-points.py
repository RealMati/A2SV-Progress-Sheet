class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points=sorted(points)
        maximumGap=0

        for idx in range(1,len(points)):

            maximumGap=max(maximumGap,points[idx][0]-points[idx-1][0])

        return maximumGap
        