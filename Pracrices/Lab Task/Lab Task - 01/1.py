minutes = eval(input("Enter the minutes: "))
years = minutes / 525600;
# 365 * 24 * 60
days = minutes / 1440;
# 24 * 60
print("Years: ", round(years))
print("Days: ", round(days))
