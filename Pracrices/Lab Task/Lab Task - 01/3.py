height = eval(input("Enter your heights (Inches): "))
weight = eval(input("Enter your weight (Pounds): "))
height1 = float(height * 0.0254)
weight1 = float(weight * 0.45359237)
bmi = weight1 / float(height1 * height1)

if bmi <= 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25 < bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")