import time


class StopWatch:
    def __init__(self):
        self.__startTime = self.getMilliseconds()
        self.__endTime = self.getMilliseconds()

    def start(self):
        self.__startTime = self.getMilliseconds()

    def stop(self):
        self.__endTime = self.getMilliseconds()

    def getElapsedTime(self):
        return self.__endTime - self.__startTime

    def getMilliseconds(self):
        return round(time.time() * 1000)


obj = StopWatch()
total = 0
for i in range(1, 1000001):
    total += i

obj.stop()
print("Elapsed time in milliseconds: ", obj.getElapsedTime())
