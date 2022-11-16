sum = 0

for i in range(1, 10001):
    for j in range(1, i):
        if(i%j == 0):
            sum += j
    if i == sum:
        print(i)
    sum = 0

# 6
# 28
# 496
# 8128