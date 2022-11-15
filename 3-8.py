import math

height = int(input("Enter height : "))
angle = int(input("Enter angle : "))

length = height/(math.sin(angle))

print("The required length is :", length)