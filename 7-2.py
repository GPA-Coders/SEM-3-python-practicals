s1 = {1, 2, 3}
s2 = {4, 5, 6}

print(s1, s2)

s1.add(4)
s2.remove(5)

print("Union :", s1.union(s2))
print("Intersection :", s1.intersection(s2))
print("Difference :", s1.difference(s2))
print("Symetric Difference :", s1.symmetric_difference(s2))
print("Subset :", s1.issubset(s2))

# {1, 2, 3} {4, 5, 6}
# Union : {1, 2, 3, 4, 6}
# Intersection : {4}
# Difference : {1, 2, 3}
# Symetric Difference : {1, 2, 3, 6}
# Subset : False