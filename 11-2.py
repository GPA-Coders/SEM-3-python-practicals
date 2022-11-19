fname = input("Enter filename : ")
f = open(fname, "r")
content = f.read()
f.close()

dictionary = {}

for alpha in content:
    if alpha in dictionary.keys():
        dictionary[alpha] += 1
    else:
        dictionary[alpha] = 1

for keys in dictionary.keys():
    print(f"{keys} - {dictionary[keys]}")

# M - 1
# y - 1
#   - 3
# n - 1
# a - 2
# m - 1
# e - 2
# i - 1
# s - 1
# H - 1
# c - 1
# k - 1
# r - 1