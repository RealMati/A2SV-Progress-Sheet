class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        res=[]
       
        for i in range(len(ranges)-1):
            if ranges[i][1]+1>=ranges[i+1][0]:
                ranges[i+1][0]=ranges[i][0]
                ranges[i+1][1]=max(ranges[i+1][1],ranges[i][1])
            else:
                res.append(ranges[i])
        
        res.append(ranges[-1])
        # print(res)
        for start,end in res:
            if start<=left<=end and start<=right<=end:
                return True
        
        return False
