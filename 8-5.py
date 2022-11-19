def GCD(n, m):
    if n == 0:
        return m
    else:
        return GCD(m%n, n)

n = int(input("Enter n : "))
m = int(input("Enter n : "))

print("GCD :", GCD(n, m))

# Enter n : 111
# Enter n : 222
# GCD : 111