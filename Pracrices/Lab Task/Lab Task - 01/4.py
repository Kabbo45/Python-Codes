year = eval(input("Enter the year: "))
x = year % 4;
if x == 0:
    print("The ", year,"is a leap year")
else:
    print("The ", year, "is not a leap year")