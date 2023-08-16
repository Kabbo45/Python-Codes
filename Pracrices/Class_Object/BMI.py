class BMI:
    def __init__(self, name, age, weight, height):
        self.bmi = 0
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculateBMI(self):
        T1 = float(self.weight * 0.45359237)
        T2 = float(self.height * 0.0254)
        return T1 / float(T2 * T2)

    def status(self):
        if self.calculateBMI() <= 18.5:
            return "Underweight"
        elif 18.5 <= self.calculateBMI() <= 24.9:
            return "Normal"
        elif 25 < self.calculateBMI() <= 29.9:
            return "Overweight"
        else:
            return "Obese"


n = input("Enter your name: ")
a = input("Enter your age: ")
w = input("Enter your weight (Pound): ")
h = input("Enter your height (Inches): ")
obj = BMI(n, a, w, h)
print(obj.status())