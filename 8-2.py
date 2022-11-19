def rem_dup(l1):
    l2 = []
    for i in l1:
        if i in l2:
            continue
        else:
            l2.append(i)
    return l2

l = [1, 1, 2, 3, 4, 6, 3, 7, 8, 3]
print(rem_dup(l))

# [1, 2, 3, 4, 6, 7, 8]