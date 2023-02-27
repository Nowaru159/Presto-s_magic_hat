year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "it isn't a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "it isn't a leap year.")
