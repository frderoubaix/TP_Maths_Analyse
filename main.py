# This is a sample Python script.
import numpy as np
from math import *
import matplotlib.pyplot as plt


def f(x):
    return sqrt(1 + x)


def Lagrange(function, borne_inf, borne_sup, degree):
    x = np.linspace(borne_inf, borne_sup, degree + 1)
    X = np.poly1d([1, 0])

    p = 0
    for i in range(0, degree + 1):
        Li = 1
        for j in range(0, degree + 1):
            if i == j:
                continue
            else:
                Li = Li * (X - x[j]) / (x[i] - x[j])
        p = p + Li * function(x[i])
    return p


PL = Lagrange(f, 0, 1, 2)

f2 = np.vectorize(f)
xp = np.linspace(0, 1, 100)

plot1 = plt.figure(1)
plt.plot(xp, f2(xp), 'r')
plt.plot(xp, PL(xp), 'g')

plot1 = plt.figure(2)
plt.plot(xp, f2(xp) - PL(xp), 'r')

plt.show()
