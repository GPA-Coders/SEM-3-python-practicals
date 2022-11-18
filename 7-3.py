d = {'a' : 1, 'b' : 2}

print(d)

d['c'] = 3
print(d)

del d['c']
print(d)

if 'b' in d.keys():
    print("B exists in dictionary")
else:
    print("B doesn't exist in dictionary")

for key, value in d.keys(), d.values():
    print(key, ":", value)

d1 = {1 : 'a'}
d2 = {2 : 'b'}
d1.update(d2)
print(d1)

# {'a': 1, 'b': 2}
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2}
# B exists in dictionary
# a : b
# 1 : 2
# {1: 'a', 2: 'b'}