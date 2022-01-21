import numpy as np
from math import *
import matplotlib.pyplot as plt

X = np.poly1d([1, 0])


def function1(x):
    if x == 0:
        return 1
    return sin(2 * pi * x) / (2 * pi * x)


def function2(x):
    return 1 / (1 + pow(x, 2))


# retourne dd les différences divisées
def diffdiv(xi, yi):
    a_result = []
    dd = [yi[0]]
    result = []
    for i in range(0, yi.__len__() - 1):
        for j in range(0, yi.__len__() - 1):
            a_result.append((yi[j] - yi[j + 1]) / (xi[j] - xi[j + (i + 1)]))
        yi = a_result.copy()
        result.append(a_result[0])
        a_result.clear()
    dd.extend(result)
    return dd


# fonction pour trouver u polynome P avec la méthode de horner
def myhorner(dd, xi):
    polynomial = dd[0]
    for i in range(1, dd.__len__()):
        polynomial = polynomial + dd[i] * concat(i, xi)
    return polynomial


# can concat (x-x1)(x-x2)...(x-xn)
def concat(i, xi, x=X):
    concat_mult = 1
    for j in range(0, i):
        concat_mult = concat_mult * (x - xi[j])
    return concat_mult


def equirepartis(a, b, i, n):
    return a + (i - 1) * ((b - a) / (n - 1))


def tchbychev(a, b, i, n):
    return ((a + b) / 2) * a + ((b - a) / 2) * cos((2 * i - 1) * (pi / (2 * n)))


def comparaison(f, a, b, n):
    xi = []
    for i in range(1, n + 1):
        xi.append(f(a, b, i, n))
    return xi


def calcul_yi(xi, f):
    yi = []
    for i in range(0, xi.__len__()):
        yi.append(f(xi[i]))
    return yi


def P1_n(n):
    P1_n_xi = comparaison(equirepartis, -5, 5, n)
    P1_n_dd = diffdiv(P1_n_xi, calcul_yi(P1_n_xi, function2))
    return myhorner(P1_n_dd, P1_n_xi)


xi = [-1, 0, 2, 5]
yi = [-2, 2, 4, 1]

# test diffdiv
dd = diffdiv(xi, yi)
print(dd)

# test myhorner
print(myhorner(dd, xi))

# test comparaison
print(comparaison(equirepartis, 0, 1, 18))
print(comparaison(tchbychev, -1, 1, 8))

# test création du polynome d'interpolation P1
P1_xi = comparaison(equirepartis, -2, 2, 2)
print(P1_xi)
P1_dd = diffdiv(P1_xi, calcul_yi(P1_xi, function1))
P1 = myhorner(P1_dd, P1_xi)

P2_xi = comparaison(tchbychev, -2, 2, 8)
P2_dd = diffdiv(P2_xi, calcul_yi(P2_xi, function1))
P2 = myhorner(P2_dd, P2_xi)

f1 = np.vectorize(function2)

plot1 = plt.figure(1)
xp = np.linspace(-5, 5)
plt.plot(xp, f1(xp), 'b')
for i in range(5, 12):
    plt.plot(xp, P1_n(i)(xp))
plt.show()

