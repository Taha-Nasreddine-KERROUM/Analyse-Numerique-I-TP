from tp3p2 import *


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

        apply_pivot_swap(mat, b, col_perm, k, pivot_i, pivot_j)

        pivot = mat[k][k]

        eliminate(mat, b, k, pivot)

        print_step_tri(mat, b, k)
        if isTriangulaireSuprieure(mat):
            break

    return mat, b, col_perm


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

    apply_pivot_swap(mat, b, col_perm, k, pivot_i, pivot_j)

    pivot = mat[k][k]

    eliminate(mat, b, k, pivot)

    print_step_tri(mat, b, k)

    return triangularisationPLREC(mat, b, k + 1, col_perm)