def isValid(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return (s*(s-side1)*(s-side2)*(s-side3))**0.5

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if isValid(side1, side2, side3):
    print("The area of the triangle is: ", area(side1, side2, side3))
else:
    print("Invalid input")



