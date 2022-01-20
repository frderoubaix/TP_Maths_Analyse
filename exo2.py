import numpy as np

X = np.poly1d([1, 0])


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
        concat_mult = concat_mult * (x-xi[j])
    return concat_mult


xi = [-1, 0, 2, 5]
yi = [-2, 2, 4, 1]

# test diffdiv
dd = diffdiv(xi, yi)
print(dd)

# test myhorner
print(myhorner(dd, xi))
