import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

def tetration(n,m):
    r = n
    for _ in range(m):
        r *= r
    return r

def df(f: Callable, x: float, fargs: list = [], h: float = 1e-10) -> float:
    expr = f(x + h, *fargs) - f(x, *fargs)
    return expr / h

def user_input():
    while True:
        m = input("Enter an integer greater then zero to tetrate to\n")
        try:
            m = int(m)
            if m > 0:
                return m
            else:
                print('m must be greater then zero')
        except ValueError:
            print('m must be an integer')

m = user_input()

t = np.linspace(-10,10, 100)
y = []
z = []

for n in t:
    y.append(tetration(n,m))
    z.append(df(tetration, n, [m]))

fig, ax = plt.subplots()

ax.set_facecolor('grey')
fig.set_facecolor('grey')

ax.plot(t, y, linewidth=2, color = 'red', label = '$f(x)$')
ax.plot(t, z, linewidth=2, color = 'blue', label = r'$\frac{df}{dx}$')
ax.legend(fontsize=14)
ax.set_title(rf'$f(x)= ^{m}x$')

plt.show()
