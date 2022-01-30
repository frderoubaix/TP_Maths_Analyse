import numpy as np
import scipy.linalg as la
from math import *

A = np.array([
                [-sin(pi/6), 0, -sin(pi/4), 0, 0, 0, 0, 0, 0, 0, 0],
                [0, -1, -cos(pi/4), 0, cos(pi/4), 1, 0, 0, 0, 0, 0],
                [0, 0, sin(pi/4), 0, sin(pi/4), 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, -cos(pi/4), 0, cos(pi/4), 1, 0, 0, 0],
                [0, 0, 0, 0, -sin(pi/4), 0, -sin(pi/4), 0, 0, 0, 0],
                [0, 0, 0, 0, 0, -1, -cos(pi/4), 0, cos(pi/4), 1, 0],
                [0, 0, 0, 0, 0, 0, sin(pi/6), 0, sin(pi/4), 0, 0],
                [0, 0, 0, 0, 0, 0, 0, -1, -cos(pi/4), 0, cos(pi/6)],
                [0, 0, 0, 0, 0, 0, 0, 0, -sin(pi/4), 0, -sin(pi/6)],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -cos(pi/6)],
                [-cos(pi/6), 0, cos(pi/4), 1, 0, 0, 0, 0, 0, 0, 0]
              ])


def factoLU(a):
    P, L, U = la.lu(a)
    return np.concatenate((L, U, P), axis=1)


def drLU(C, b):
    lu = np.hsplit(C, 3)
    final_lu = np.add(lu[1], lu[0]) - lu[2]
    piv = la.lu_factor(A)
    return la.lu_solve((final_lu, piv[1]), b)


# test facto LU
LU = factoLU(A)
print(LU)

# test drLU
b = np.array([
                [0],
                [0],
                [10000],
                [0],
                [0],
                [0],
                [20000],
                [0],
                [0],
                [0],
                [0]
])
result = drLU(LU, b)

print(result)
