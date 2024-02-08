class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx=0
        for passenger, start, end in trips:
            maxx=max(maxx,end)
        prefix=[0]*(maxx+1)

        for passenger, start, end in trips:
            prefix[start]+=passenger
            if end<len(prefix): prefix[end]+=passenger*-1

        if prefix[0]>capacity: return False
        
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
            if prefix[i]>capacity: return False

        return True