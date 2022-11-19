import math

def mean(l):
    return sum(l)/len(l)

def deviation(l):
    sum = 0
    for i in l:
        sum += pow((i - mean(l)), 2)
    
    div = sum/(len(l) - 1)
    return math.sqrt(div)

n = int(input("Enter n : "))
l = []
for i in range(n):
    num = int(input("Enter number : "))
    l.append(num)

print("\nMean :", mean(l))
print("Deviation :", deviation(l))

# Enter n : 5
# Enter number : 1
# Enter number : 2
# Enter number : 3
# Enter number : 4
# Enter number : 5

# Mean : 3.0
# Deviation : 1.5811388300841898