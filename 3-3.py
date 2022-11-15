p = int(input("Enter principal : "))
r = int(input("Enter rebate : "))
n = int(input("Enter periods of interest : "))
t = int(input("Enter time in years : "))

simple = (p * r * t)/100
compound = ((1 + (r/(100 * n))) ** (n*t)) * p

print("The simple interest is :", simple)
print("The compound interest is :", compound - p)