n = eval(input("Enter n: "))

for x in range(2, 100):
    y = n % x;
    if y == 0:
        print("Smallest Factor of", n, " is: ", x)
        break