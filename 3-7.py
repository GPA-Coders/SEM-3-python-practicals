import math

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

d = (math.pow(b, 2)) - (4 * a * c)

root1 = (-b + math.sqrt(d))/(2*a)
root2 = (-b - math.sqrt(d))/(2*a)

print("The roots are :", root1, root2)