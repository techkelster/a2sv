class UndergroundSystem:

    def __init__(self):
        self.checkedIns = {}
        self.travels = {}
        self.times = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIns[id] = (stationName, t)
    

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.checkedIns[id][0], stationName) in self.travels:
            self.travels[(self.checkedIns[id][0], stationName)] +=(t - self.checkedIns[id][1])
        else:
            self.travels[(self.checkedIns[id][0], stationName)] = (t - self.checkedIns[id][1])
        if (self.checkedIns[id][0], stationName) in self.times:
            self.times[(self.checkedIns[id][0], stationName)] += 1
        else:
            self.times[(self.checkedIns[id][0], stationName)] = 1
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (self.travels[(startStation, endStation)] / self.times[(startStation, endStation)])

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)