import random

l = []

for i in range(4):
    temp = []
    for i in range(4):
        temp.append(random.randint(0, 1))
    l.append(temp)

for i in range(4):
    for j in range(4):
        print(l[i][j], end=" ")
    print()

row_count = [0, 0, 0, 0]
col_count = [0, 0, 0, 0]

for i in range(4):
    for j in range(4):
        if l[i][j] == 1:
            row_count[i] += 1
        if l[j][i] == 1:
            col_count[i] += 1

print("\nRow with highest 1s :", row_count.index(max(row_count))+1)
print("Column with highest 1s :", col_count.index(max(col_count))+1)

# 1 0 0 0 
# 1 1 1 1 
# 1 1 1 0 
# 0 0 1 1 

# Row with highest 1s : 2
# Column with highest 1s : 1