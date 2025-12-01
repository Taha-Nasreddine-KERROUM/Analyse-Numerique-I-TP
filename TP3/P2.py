from P1 import *

def triangularisationPP(mat, b):
    n = len(mat)
    print_system(mat, b)
    for k in range(n):
        p = abs(mat[k][k])
        l = k
        for i in range(k, n):
            if abs(mat[i][k]) > p:
                p = abs(mat[i][k])
                l = i

        if l != k:
            for j in range(k, n):
                mat[k][j], mat[l][j] = mat[l][j], mat[k][j]
            b[k], b[l] = b[l], b[k]

        eliminate(mat, b, k, mat[k][k])

        print_step_tri(mat, b, k)

        if isTriangulaireSuprieure(mat):
            return mat, b

    print_gauss_header(mat, b)

    return mat, b


def pivotSearchHelper(mat, k, n):
    p = abs(mat[k][k])
    l = k
    for i in range(k, n):
        if abs(mat[i][k]) > p:
            p = abs(mat[i][k])
            l = i
    return l


def swapRowsHelper(mat, b, k, l, n):
    for j in range(k, n):
        mat[k][j], mat[l][j] = mat[l][j], mat[k][j]
    b[k], b[l] = b[l], b[k]


def triangularisationPPREC(mat, b, k=0):
    n = len(mat)

    if k == 0:
        print_system(mat, b)

    if k >= n or isTriangulaireSuprieure(mat):
        print_gauss_header(mat, b)
        return mat, b

    l = pivotSearchHelper(mat, k, n)

    if l != k:
        swapRowsHelper(mat, b, k, l, n)

    eliminate(mat, b, k, mat[k][k])

    print_step_tri(mat, b, k)

    return triangularisationPPREC(mat, b, k + 1)