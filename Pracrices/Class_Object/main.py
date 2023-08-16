class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __del__(self):
        print("Object Destroyed")

    def show(self):
        return 0.5 * self.base * self.height

obj = Triangle(10, 20)
print(obj.show())

obj.base = 10.5
obj.height = 20.5
print(obj.show())
del obj