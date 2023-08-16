def numberOfDays(year):
    if year % 4 == 0:
        return 366
    else:
        return 365


start = 2010
end = 2020
y = 0
for year in range(start, end+1):
    x = numberOfDays(year)
    print(year, " has ", x, " days")
    y = y+x

print("Sum of the days: ", y)


