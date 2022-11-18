tup = (1, "string", 1.5)

print(tup)

tup_list = list(tup)

tup_list.remove("string")

tup = tuple(tup_list)

print(tup)

# (1, 'string', 1.5)
# (1, 1.5)