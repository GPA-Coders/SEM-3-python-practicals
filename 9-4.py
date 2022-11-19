import matplotlib.pyplot as mp

l = []

for i in range(-5, 6):
    l.append(max(0, i))

mp.plot(l)
mp.show()