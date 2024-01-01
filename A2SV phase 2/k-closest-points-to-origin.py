class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for idx,pt in enumerate(points):
            points[idx]=[pt,pt[0]**2+pt[1]**2]
        
        sorted_points=sorted(points, key=lambda x:x[1])
        res=[]
        for pt,distance in sorted_points:
            res.append(pt)
            if len(res)==k:
                return res
        return res