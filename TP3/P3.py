from P2 import *


def triangularisationPL(mat, b):
    n = len(mat)
    col_perm = list(range(n))
    print_system(mat, b)

    for k in range(n):
        pivot_value = 0
        pivot_i, pivot_j = k, k

        for i in range(k, n):
            for j in range(k, n):
                if abs(mat[i][j]) > pivot_value:
                    pivot_value = abs(mat[i][j])
                    pivot_i, pivot_j = i, j

        if pivot_i != k:
            mat[k], mat[pivot_i] = mat[pivot_i], mat[k]
            b[k], b[pivot_i] = b[pivot_i], b[k]

        if pivot_j != k:
            for i in range(n):
                mat[i][k], mat[i][pivot_j] = mat[i][pivot_j], mat[i][k]
            col_perm[k], col_perm[pivot_j] = col_perm[pivot_j], col_perm[k]

        pivot = mat[k][k]

        eliminate(mat, b, k, pivot)

        print_step_tri(mat, b, k)
        if isTriangulaireSuprieure(mat):
            break

    return mat, b, col_perm


def reorder_x_after_column_swaps(x_perm, col_perm):
    n = len(x_perm)
    x_orig = [0 for _ in range(n)]

    for k in range(n):
        x_orig[col_perm[k]] = x_perm[k]

    print("Solution dans l'ordre original :")
    print_step_rem(x_orig)

    return x_orig


def finding_pivot(mat, k):
    n = len(mat)
    pivot_value = 0
    pivot_i, pivot_j = k, k
    for i in range(k, n):
        for j in range(k, n):
            if abs(mat[i][j]) > pivot_value:
                pivot_value = abs(mat[i][j])
                pivot_i, pivot_j = i, j
    return pivot_value, pivot_i, pivot_j


def swapCol(mat, col_perm, k, pivot_j):
    n = len(mat)
    for i in range(n):
        mat[i][k], mat[i][pivot_j] = mat[i][pivot_j], mat[i][k]
    col_perm[k], col_perm[pivot_j] = col_perm[pivot_j], col_perm[k]


def triangularisationPLREC(mat, b, k=0, col_perm=None):
    n = len(mat)
    if col_perm is None:
        col_perm = list(range(n))

    if k == 0:
        print_system(mat, b)

    if k == n or isTriangulaireSuprieure(mat):
        print_gauss_header(mat, b)
        return mat, b, col_perm

    pivot_value, pivot_i, pivot_j = finding_pivot(mat, k)

    if pivot_i != k:
        mat[k], mat[pivot_i] = mat[pivot_i], mat[k]
        b[k], b[pivot_i] = b[pivot_i], b[k]

    if pivot_j != k:
        swapCol(mat, col_perm, k, pivot_j)

    pivot = mat[k][k]

    eliminate(mat, b, k, pivot)

    print_step_tri(mat, b, k)

    return triangularisationPLREC(mat, b, k + 1, col_perm)