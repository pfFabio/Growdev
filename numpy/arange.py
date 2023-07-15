import numpy as np

vetor = np.arange(1,10)

print(vetor)

def f(x):
    return x**2 + 1

print(f(vetor))

def baskara(a, b, c):
    delta = b**2 - 4*a*c
    x1=(-b - np.sqrt(delta))/2*a
    print(x1)



baskara(1,1,-1)


print(np.sqrt(4))