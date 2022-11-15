year = int(input("Enter year : "))

if year%4 == 0 and year%400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

# Enter year : 2022
# It is not a leap year