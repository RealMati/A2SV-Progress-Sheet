class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix=[0]*(n+1)

        for start, end, val in bookings:
            prefix[start-1]+=val
            prefix[end]+=val*-1
        
        for i in range(1,n+1):
            prefix[i]+=prefix[i-1]
        
        prefix.pop()
        return prefix