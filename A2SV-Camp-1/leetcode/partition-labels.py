class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}

        for idx,chr in enumerate(s):
            if chr not in dic:
                dic[chr]=[idx,idx]
            else:
                dic[chr][1]=idx
        intervals=sorted(dic.values())
        res=[]

        for i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1][0]=intervals[i][0]
                intervals[i+1][1]=max(intervals[i+1][1],intervals[i][1])
            else:
                res.append(intervals[i][1]-intervals[i][0]+1)
        
        res.append(intervals[-1][1]-intervals[-1][0]+1)
        return res
