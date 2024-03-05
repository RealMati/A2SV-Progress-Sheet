class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res=len(timeSeries)*duration

        for i in range(1,len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1]<duration:
                res-= duration-(timeSeries[i]-timeSeries[i-1])
                
        return res
