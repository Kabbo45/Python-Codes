class Time:
    def __init__(self):
        import time
        self.hour = int(time.strftime('%H'))
        self.minute = int(time.strftime('%M'))
        self.second = int(time.strftime('%S'))

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setTime(self, elapsedTime):
        total_seconds = elapsedTime % 86400
        self.hour = total_seconds // 3600
        self.minute = (total_seconds % 3600) // 60
        self.second = (total_seconds % 3600) % 60


obj = Time()
print("Current time: ", obj.getHour(), ":", obj.getMinute(), ":", obj.getSecond())
elapsedTime = int(input("Enter elapsed time in seconds: "))
obj.setTime(elapsedTime)
print("New time: ", obj.getHour(), ":", obj.getMinute(), ":", obj.getSecond())
#484090