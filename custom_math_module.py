def addition(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def modulo(a, b):
    return a%b

def square(a):
    return a*a

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)