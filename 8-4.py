def is_prime(n):
    if n < 2:
        print("The number is not prime")
    for i in range(2, n):
        if n%i == 0:
            print("The number is not prime")
            exit()
    print("The number is prime")

num = int(input("Enter number : "))
is_prime(num)

# Enter number : 37
# The number is prime