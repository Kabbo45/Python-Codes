class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n

    def setN(self, n):
        self.__n = n

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        import math
        return (self.__n * self.__side ** 2) / (4 * math.tan(3.1416 / self.__n))


a = RegularPolygon()
b = RegularPolygon(6, 4)
c = RegularPolygon(10, 4, 5.6, 7.8)
print("Polygon 1:\nPerimeter:", a.getPerimeter(), "\nArea:", a.getArea())
print("\nPolygon 2:\nPerimeter:", b.getPerimeter(), "\nArea:", b.getArea())
print("\nPolygon 3:\nPerimeter:", c.getPerimeter(), "\nArea:", c.getArea())
