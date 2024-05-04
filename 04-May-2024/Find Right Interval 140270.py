# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)

        res=[-1]*len(intervals)
        intervals.sort()

        def check(idx, end):
            return intervals[idx][0]>=end

        # print(intervals)
        for i, interval in enumerate(intervals):
            start, end, idx=interval
            l=i
            r=len(intervals)-1

            while l<=r:
                mid=(l+r)//2
                
                if check(mid, end):
                    r=mid-1
                    # print(end, mid, "y")
                else:
                    l=mid+1
                    # print(end, mid, "n")

            # print(end, interval[l] if l<len(intervals) else str(l)+"l")
            res[idx]=intervals[l][-1] if l<len(intervals) else -1

        return res
                    

