class Rectangle:
    width = 1
    height = 2

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


obj = Rectangle(4, 40)
print('Area: ', obj.getArea())
print('Perimeter: ', obj.getPerimeter())

obj = Rectangle(3.5, 35.7)
print('Area: ', obj.getArea())
print('Perimeter: ', obj.getPerimeter())