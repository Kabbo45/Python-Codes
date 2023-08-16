def sort(num1, num2):
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1


n1, n2 = sort(5, 4)
print("num1 is: ", n1)
print("num2 is: ", n2)


def f(x, y):
    return x + y, x - y, x * y, x / y


t1, t2, t3, t4 = f(5, 4)
print(t1, t2, t3, t4)
