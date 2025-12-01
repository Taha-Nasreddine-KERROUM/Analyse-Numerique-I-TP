from tp2 import *


def triangularisation(mat, b):
    n = len(mat)
    print_system(mat, b)

    if null_in_diagonal(mat):
        print('null detected')
        return None, None

    for k in range(n - 1):
        pivote = mat[k][k]

        eliminate(mat, b, k, pivote)

        print_step_tri(mat, b, k)
        if isTriangulaireSuprieure(mat):
            break

    print_gauss_header(mat, b)
    return mat, b


def triangularisationREC(mat, b, k=0):
    n = len(mat)

    if k == 0:
        print_system(mat, b)
        if null_in_diagonal(mat):
            print('null detected')
            return None, None

    if k >= n - 1 or isTriangulaireSuprieure(mat):
        print_gauss_header(mat, b)
        return mat, b

    pivote = mat[k][k]
    if pivote != 0:
        eliminate(mat, b, k, pivote)

    print_step_tri(mat, b, k)
    return triangularisationREC(mat, b, k + 1)