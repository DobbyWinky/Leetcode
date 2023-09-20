class UndergroundSystem:

    def __init__(self):
        self.checkin={}
        self.time={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(stationName, t)
        

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        startStation, startTime=self.checkin[id]
        if (startStation, endStation) not in self.time:
            self.time[(startStation, endStation)]=[0,0]
        self.time[(startStation, endStation)][1]+=1
        self.time[(startStation, endStation)][0]+=endTime-startTime
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time[(startStation, endStation)][0]/self.time[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)