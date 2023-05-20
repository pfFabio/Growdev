import matplotlib.pyplot as plt
from random import randint
x = []
y = []
r = randint(0, 20)

for i in range(50):
    x.append(i)
    r += randint(-2, 2)
    y.append(r)

plt.plot(x, y)
plt.show()
