l = []
n = int(input("Enter n : "))

for i in range(n):
    num = int(input("Enter number : "))
    l.append(num)

positive = 0
negative = 0
zeroes = 0
odd = 0
even = 0
sum = 0

for num in l:
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1
    if num == 0:
        zeroes += 1
    if num > 0 and num%2 == 1:
        odd += 1
    if num > 0 and num%2 == 0:
        even += 1
    sum += num

print("\nNegative numbers :", negative)
print("Positive numbers :", positive)
print("Zeroes :", zeroes)
print("Odd numbers :", odd)
print("Even numbers :", even)
print("Average :", sum/n)

# Enter n : 5
# Enter number : -1
# Enter number : 1
# Enter number : 0
# Enter number : 5
# Enter number : 2

# Negative numbers : 1
# Positive numbers : 3
# Zeroes : 1
# Odd numbers : 2
# Even numbers : 1
# Average : 1.4