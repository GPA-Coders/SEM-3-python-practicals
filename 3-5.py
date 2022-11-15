a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

print("a is greatest" if (a > b and a > c) else "b is greatest" if b > a and b > c else "c is greatest")