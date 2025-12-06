from helpers import *


def descenteITR(mat, b):
    if isTriangulaireSuprieure(mat) == True:
        print('must be inf')
        return None

    n = len(mat)
    x = []
    x.append(b[0] / mat[0][0])

    return substitution(
        mat,
        b,
        x,
        i_range=range(1, n),
        j_range=lambda i: range(i - 1, -1, -1)
    )

def descenteREC(mat, b, i=0, j=None, x=None, somme=0):
    if isTriangulaireSuprieure(mat) == True:
        print('must be inf')
        return None

    if x is None:
        x = [0.0] * len(mat)
    if j is None:
        j = i - 1

    if i == len(mat):
        return x

    if j >= 0:
        return descenteREC(mat, b, i, j - 1, x, somme + mat[i][j] * x[j])
    else:
        x[i] = (b[i] - somme) / mat[i][i]
        return descenteREC(mat, b, i + 1, None, x, 0)

def remontéeITR(mat, b):
    if isTriangulaireInfrieure(mat) == True:
        print('must be sup')
        return None

    n = len(mat)
    x = [0] * n

    if mat[n - 1][n - 1] == 0:
        print("mat[", n - 1, "][", n - 1, "] = 0")
        return None

    x[n - 1] = b[n - 1] / mat[n - 1][n - 1]

    x = substitution(
        mat,
        b,
        x,
        i_range=range(n - 2, -1, -1),
        j_range=lambda i: range(i + 1, n)
    )

    print_step_rem(x)
    return x


def remontéeREC(mat, b, i=None, j=None, x=None, somme=0):
    if isTriangulaireInfrieure(mat) == True:
        print('must be sup')
        return None

    n = len(b)
    if x is None:
        x = [0.0] * n
    if i is None:
        i = n - 1
    if j is None:
        j = i + 1

    if i < 0:
        return x

    if j < n:
        return remontéeREC(mat, b, i, j + 1, x, somme + mat[i][j] * x[j])
    else:
        x[i] = (b[i] - somme) / mat[i][i]
        return remontéeREC(mat, b, i - 1, None, x, 0)


def Cramer(mat, b):
    if determinantIterative(mat) == 0:
        return None

    n = len(mat)
    x = []

    for i in range(n):
        submat = copyMat(mat, i, b)
        x.append(determinantIterative(submat) / determinantIterative(mat))

    return x


def RECramer(mat, b, i=0, x=None, detA=None):
    n = len(mat)
    if x is None:
        x = []
    if detA is None:
        detA = determinantIterative(mat)
        if detA == 0:
            return None

    if i == n:
        return x

    submat = copyMat(mat, i, b)
    x.append(determinantIterative(submat) / detA)
    return RECramer(mat, b, i + 1, x, detA)


def order(A, b, col_perm):
    x = remontéeITR(A, b)
    reorder_x_after_column_swaps(x, col_perm)