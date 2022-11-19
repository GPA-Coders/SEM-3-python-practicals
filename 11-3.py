f = open("11-3.txt", "r")
content = f.read()
f.close()

for i in content:
    if i.isdigit():
        print(i, end = " ")

# 1 2 1 2 3 4 5