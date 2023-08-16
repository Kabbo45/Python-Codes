def displaySortedNumbers(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        if num2 < num3:
            return num1, num2, num3
        else:
            return num1, num3, num2
    elif (num2 < num2) and (num2 < num3):
        if num1 < num3:
            return num2, num1, num3
        else:
            return num2, num3, num1
    elif (num3 < num1) and (num3 < num2):
        if num1 < num2:
            return num3, num1, num2
        else:
            return num3, num2, num1

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
print("Sorted numbers: ",displaySortedNumbers(num1, num2, num3))

