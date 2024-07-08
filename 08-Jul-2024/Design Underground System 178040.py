# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.trips=defaultdict(int)
        self.tripCt=defaultdict(int)
        self.inboard={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inboard[id]=[stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.trips[self.inboard[id][0], stationName]+= t-self.inboard[id][1]
        self.tripCt[self.inboard[id][0], stationName]+=1
        del self.inboard[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.trips[startStation, endStation]/self.tripCt[startStation, endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)