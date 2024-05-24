# Problem: Merge Interval - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]

        for i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1][0]=intervals[i][0]
                intervals[i+1][1]=max(intervals[i+1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        
        res.append(intervals[-1])
        return res
