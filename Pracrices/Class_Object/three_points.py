class Points:
    def __init__(self, xx1, xx2, xx3, yy1, yy2, yy3):
        self.xx1 = xx1
        self.xx2 = xx2
        self.xx3 = xx3
        self.yy1 = yy1
        self.yy2 = yy2
        self.yy3 = yy3

    def calcul(self):
        return float(0.5 * (self.xx1 * (self.yy2 - self.yy3) + self.xx2 * (self.yy3 - self.yy1) + self.xx3 * (self.yy1 - self.yy2)))


x1, y1 = eval(input("Enter x1,y1: "))
x2, y2 = eval(input("Enter x2,y2: "))
x3, y3 = eval(input("Enter x3,y3: "))
obj = Points(x1, x2, x3, y1, y2, y3)
print(obj.calcul())
