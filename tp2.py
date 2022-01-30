import numpy as np
import scipy.linalg as la

A = np.array([[1, 1, 1],
              [-1, 1, 1],
              [1, 2, 3]])


def factoLU(a):
    P, L, U = la.lu(a)
    return np.concatenate((L, U), axis=1)


def drLU(C, b):
    lu = np.hsplit(C, 2)
    lu = lu[1] + lu[0]
    print(lu)
    # return la.lu_solve(lu, b)



# test facto LU
LU = factoLU(A)
print(LU)

# test drLU
b = np.array([[1],
              [3],
              [6]])
lu, piv = la.lu_factor(A)
drLU(LU, b)
print(lu)
