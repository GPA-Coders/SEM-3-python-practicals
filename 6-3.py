l = list(input("Enter string : "))
count = []

for i in l:
    if i in count:
        count[count.index(i) + 1] += 1
    else:
        count.append(i)
        count.append(1)

print()

for i in range(0, len(count), 2):
    print(count[i], "=", count[i+1], "times")

# Enter string : 12203AB3

# 1 = 1 times
# 2 = 2 times
# 0 = 1 times
# 3 = 2 times
# A = 1 times
# B = 1 times