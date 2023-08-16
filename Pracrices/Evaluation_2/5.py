class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def geta(self):
        return self.__a

    def getb(self, b):
        return self.__b

    def getc(self, c):
        return self.__c

    def getd(self, d):
        return self.__d

    def gete(self, e):
        return self.__e

    def getf(self, f):
        return self.__f

    def isSolvable(self):
        return (self.__a * self.__d) - (self.__b * self.__c) != 0

    def getX(self):
        t1 = (self.__e * self.__d) - (self.__b * self.__f)
        t2 = (self.__a * self.__d) - (self.__b * self.__c)
        return t1/t2

    def getY(self):
        l1 = (self.__a * self.__f) - (self.__e * self.__c)
        l2 = (self.__a * self.__d) - (self.__b * self.__c)
        return l1/l2


a1, b1, c1, d1, e1, f1 = eval(input("Enter values of a, b, c, d, e, f: "))
obj = LinearEquation(a1, b1, c1, d1, e1, f1)
if obj.isSolvable():
    print("X = ", obj.getX(), "\nY = ", obj.getY())
else:
    print("The equation has no solution.")