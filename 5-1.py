n = int(input("Enter number of inputs : "))

sum = 0
avg = 0

for i in range(n):
    num = int(input("Enter number : "))
    sum += num

avg = sum/n

print("\nThe average is :", avg)

# Enter number of inputs : 5
# Enter number : 1
# Enter number : 2
# Enter number : 3
# Enter number : 4
# Enter number : 5
#
# The average is : 3.0