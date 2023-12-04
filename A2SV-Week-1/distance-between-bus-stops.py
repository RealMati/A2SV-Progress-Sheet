class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        summ=sum(distance)
        if start>destination:
            start,destination=destination,start
        d=sum(distance[start:destination])
        return min(summ-d,d)
        