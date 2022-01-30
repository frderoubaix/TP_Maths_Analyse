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


def P1_n_function1(n):
    P1_n_xi = comparaison(equirepartis, -2, 2, n)
    P1_n_dd = diffdiv(P1_n_xi, calcul_yi(P1_n_xi, function1))
    return myhorner(P1_n_dd, P1_n_xi)


def P2_n_function1(n):
    P2_n_xi = comparaison(tchbychev, -2, 2, n)
    P2_n_dd = diffdiv(P2_n_xi, calcul_yi(P2_n_xi, function1))
    return myhorner(P2_n_dd, P2_n_xi)


def P1_n_function2(n):
    P1_n_xi = comparaison(equirepartis, -5, 5, n)
    P1_n_dd = diffdiv(P1_n_xi, calcul_yi(P1_n_xi, function2))
    return myhorner(P1_n_dd, P1_n_xi)


def P2_n_function2(n):
    P2_n_xi = comparaison(tchbychev, -5, 5, n)
    P2_n_dd = diffdiv(P2_n_xi, calcul_yi(P2_n_xi, function2))
    return myhorner(P2_n_dd, P2_n_xi)


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
f1 = np.vectorize(function1)
f2 = np.vectorize(function2)


xp1 = np.linspace(-2, 2)
xp2 = np.linspace(-5, 5)
# P1 equirépartis et fonction 1
plot1 = plt.figure(1)
plt.plot(xp1, f1(xp1), 'b')
for i in range(5, 12):
    plt.plot(xp1, P1_n_function1(i)(xp1))

# P2 Tchebychev et fonction 1
plot1 = plt.figure(2)
plt.plot(xp1, f1(xp1), 'b')
for i in range(5, 12):
    plt.plot(xp1, P2_n_function1(i)(xp1))

# P1 equirépartis et fonction 2
plot1 = plt.figure(3)
plt.plot(xp2, f2(xp2), 'b')
for i in range(5, 12):
    plt.plot(xp2, P1_n_function2(i)(xp2))

# P2 Tchebychev et fonction 2
plot1 = plt.figure(4)
plt.plot(xp2, f2(xp2), 'b')
for i in range(5, 12):
    plt.plot(xp2, P2_n_function2(i)(xp2))

plt.show()
