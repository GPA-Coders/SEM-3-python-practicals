l = [1, 2, 3, 1, 4, 5, 2, 8, 3, 3]
n = []

for i in l:
    if i in n:
        continue
    else:
        n.append(i)

l = n

print(l)

# [1, 2, 3, 4, 5, 8]