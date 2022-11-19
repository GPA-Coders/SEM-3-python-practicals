def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter n : "))
for i in range(n):
    print(fibonacci(i), end=" ")

# Enter n : 10
# 1 1 2 3 5 8 13 21 34 55