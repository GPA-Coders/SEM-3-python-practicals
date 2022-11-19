import random

def shuffle(l1):
    length = len(l1)
    new = []
    for i in range(length):
        element = random.choice(l1)
        new.append(element)
        l1.remove(element)
    return new


l = [1, 2, 3, 4]

new = shuffle(l)
print(new)

# [4, 1, 2, 3]