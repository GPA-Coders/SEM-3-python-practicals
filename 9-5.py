from matplotlib import pyplot as plt
from random import randint
a = []
for i in range(100):
    a.append(randint(1, 10))

fig, ax = plt.subplots(figsize =(5, 10))
ax.hist(a, bins=[1,2,3,4,5,6,7,8,9,10])

plt.show()