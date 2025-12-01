import time

def print_system(mat, b):
    print("Le système est :")
    n = len(mat)
    for i in range(n):
        print(f"[ {' '.join([f'{mat[i][j]:.4f}' for j in range(n)])} ] [ {b[i]:.4f} ]")
    print()


def print_step_tri(mat, b, k):
    print(f"* Itération K= {k} :")
    print_system(mat, b)


def print_step_rem(x):
    print("* La resolution donne :")
    for i in range(len(x)):
        print(f"X_{i + 1} = {x[i]:.6f} ;")
    print()


def print_gauss_header(mat, b):
    print("-------------- Gauss ---------------")
    print("* La matrice reduite :")
    print_system(mat, b)


def triangularisation(mat, b):
    n = len(mat)
    print_system(mat, b)

    for k in range(n - 1):
        pivote = mat[k][k]
        if pivote != 0:
            for i in range(k + 1, n):
                q = mat[i][k]
                mat[i][k] = 0
                b[i] = b[i] - (q / pivote) * b[k]
                for j in range(k + 1, n):
                    mat[i][j] = mat[i][j] - mat[k][j] * (q / pivote)
        else:
            print(f"pivot {pivote} = 0")
            return None

        print_step_tri(mat, b, k)

    print_gauss_header(mat, b)
    return mat, b


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

        for i in range(k + 1, n):
            q = mat[i][k]
            mat[i][k] = 0
            for j in range(k + 1, n):
                mat[i][j] = mat[i][j] - mat[k][j] * q / mat[k][k]
            b[i] = b[i] - b[k] * q / mat[k][k]

        print_step_tri(mat, b, k)

    print_gauss_header(mat, b)

    return mat, b


def triangularisationPL(mat, b):
    n = len(mat)
    col_perm = list(range(n))

    for k in range(n):
        pivot_value = 0
        pivot_i, pivot_j = k, k

        for i in range(k, n):
            for j in range(k, n):
                if abs(mat[i][j]) > pivot_value:
                    pivot_value = abs(mat[i][j])
                    pivot_i, pivot_j = i, j

        if pivot_value == 0:
            print(f"nulle à k = {k}")
            return None, None, None

        if pivot_i != k:
            mat[k], mat[pivot_i] = mat[pivot_i], mat[k]
            b[k], b[pivot_i] = b[pivot_i], b[k]

        if pivot_j != k:
            for i in range(n):
                mat[i][k], mat[i][pivot_j] = mat[i][pivot_j], mat[i][k]
            col_perm[k], col_perm[pivot_j] = col_perm[pivot_j], col_perm[k]

        pivot = mat[k][k]
        if pivot == 0:
            print(f"Pivot nul après permutations à k = {k}")
            return None, None, None

        for i in range(k + 1, n):
            c = mat[i][k] / pivot
            b[i] -= c * b[k]
            mat[i][k] = 0
            for j in range(k + 1, n):
                mat[i][j] -= c * mat[k][j]

    return mat, b, col_perm


def reorder_x_after_column_swaps(x_perm, col_perm):
    n = len(x_perm)
    x_orig = [0 for _ in range(n)]

    for k in range(n):
        x_orig[col_perm[k]] = x_perm[k]

    print("Solution dans l'ordre original :")
    print_step_rem(x_orig)

    return x_orig


def remontee(mat, b):
    n = len(mat)
    x = [0] * n
    if mat[n - 1][n - 1] == 0:
        print("mat[", n - 1, "][", n - 1, "] = 0")
        return None

    x[n - 1] = b[n - 1] / mat[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        somme = 0
        for k in range(i + 1, n):
            somme += mat[i][k] * x[k]

        if mat[i][i] == 0:
            print("mat[", i, "][", i, "] = 0")
            return None

        x[i] = (b[i] - somme) / mat[i][i]

    print_step_rem(x)
    return x


def triHelper(mat, b, k, pivote):
    n = len(mat)
    for i in range(k + 1, n):
        q = mat[i][k]
        mat[i][k] = 0
        b[i] = b[i] - (q / pivote) * b[k]
        for j in range(k + 1, n):
            mat[i][j] = mat[i][j] - mat[k][j] * (q / pivote)


def remHelper(mat, x, i, n):
    somme = 0
    for k in range(i + 1, n):
        somme += mat[i][k] * x[k]
    return somme


def triangularisationREC(mat, b, k=0):
    n = len(mat)

    if k == 0:
        print_system(mat, b)

    if k >= n - 1:
        print_gauss_header(mat, b)
        return mat, b

    pivote = mat[k][k]
    if pivote != 0:
        triHelper(mat, b, k, pivote)

    print_step_tri(mat, b, k)
    return triangularisationREC(mat, b, k + 1)


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


def eliminateRowHelper(mat, b, k, n):
    for i in range(k + 1, n):
        q = mat[i][k]
        mat[i][k] = 0
        for j in range(k + 1, n):
            mat[i][j] = mat[i][j] - mat[k][j] * q / mat[k][k]
        b[i] = b[i] - b[k] * q / mat[k][k]


def triangularisationPPREC(mat, b, k=0):
    n = len(mat)

    if k == 0:
        print_system(mat, b)

    if k >= n:
        print_gauss_header(mat, b)
        return mat, b

    l = pivotSearchHelper(mat, k, n)

    if l != k:
        swapRowsHelper(mat, b, k, l, n)

    if mat[k][k] == 0:
        print(f"pivot {mat[k][k]} = 0")
        return None


    eliminateRowHelper(mat, b, k, n)

    print_step_tri(mat, b, k)

    return triangularisationPPREC(mat, b, k + 1)


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


def eliminate(mat, b, k, pivot):
    n = len(mat)
    for i in range(k + 1, n):
        c = mat[i][k] / pivot
        b[i] -= c * b[k]
        mat[i][k] = 0
        for j in range(k + 1, n):
            mat[i][j] -= c * mat[k][j]


def triangularisationPLREC(mat, b, k=0, col_perm=None):
    n = len(mat)
    if col_perm is None:
        col_perm = list(range(n))

    if k == 0:
        print_system(mat, b)

    if k == n:
        print_gauss_header(mat, b)
        return mat, b, col_perm

    pivot_value, pivot_i, pivot_j = finding_pivot(mat, k)

    if pivot_value == 0:
        print(f"nulle à k = {k}")
        return None, None, None

    if pivot_i != k:
        mat[k], mat[pivot_i] = mat[pivot_i], mat[k]
        b[k], b[pivot_i] = b[pivot_i], b[k]

    if pivot_j != k:
        swapCol(mat, col_perm, k, pivot_j)

    pivot = mat[k][k]

    if pivot == 0:
        print(f"Pivot nul à k = {k}")
        return None, None, None

    eliminate(mat, b, k, pivot)

    print_step_tri(mat, b, k)

    return triangularisationPLREC(mat, b, k + 1, col_perm)


def remonteeREC(mat, b, i=None, x=None):
    n = len(mat)
    if x is None:
        x = [0] * n
        i = n - 1

    if i < 0:
        print_step_rem(x)
        return x

    somme = remHelper(mat, x, i, n)

    if mat[i][i] == 0:
        print("mat[", i, "][", i, "] = 0")
        return None
    x[i] = (b[i] - somme) / mat[i][i]

    return remonteeREC(mat, b, i - 1, x)


def lireMat(n):
    return [[float(input(f"A[{i}][{j}] = ")) for j in range(n)] for i in range(n)]


def lireb(n):
    return [float(input(f"b[{i}] = ")) for i in range(n)]


from P3 import *

import time

def main():
    while True:
        n = int(input("Entrez la taille de la matrice : "))

        A = lireMat(n)
        b = lireb(n)

        method = int(input("Choisissez la méthode (1-Normal, 2-Pivot Partiel, 3-Pivot Total) : "))
        choice = int(input("Choisissez (1-Itérative, 2-Récursive) : "))

        start_time = time.time()

        if method == 1:
            if choice == 1:
                print("\n--- Méthode Normale Itérative ---\n")
                A, b = triangularisation(A, b)
                remontee(A, b)
            else:
                print("\n--- Méthode Normale Récursive ---\n")
                A, b = triangularisationREC(A, b)
                remonteeREC(A, b)

        elif method == 2:
            if choice == 1:
                print("\n--- Méthode Pivot Partiel Itérative ---\n")
                A, b = triangularisationPP(A, b)
                remontee(A, b)
            else:
                print("\n--- Méthode Pivot Partiel Récursive ---\n")
                A, b = triangularisationPPREC(A, b)
                remonteeREC(A, b)

        elif method == 3:
            if choice == 1:
                print('\n--- Méthode Pivot Total Itérative ---\n')
                A, b, col_perm = triangularisationPL(A, b)
                A, b = remontee(A, b)
                reorder_x_after_column_swaps(A, col_perm)

            if choice == 2:
                print('\n--- Méthode Pivot Total Récursive ---\n')
                A, b, col_perm = triangularisationPLREC(A, b)
                A, b = remontee(A, b)
                reorder_x_after_column_swaps(A, col_perm)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"execution time : {execution_time:.3f} s")
        input("Press any key to continue.")
        continue

#main()
def test():
    A = [[10, 5, 5, 0],
         [ 2, 5, 7, 4],
         [ 4, 4, 1, 4],
         [-2,-2, 1,-3]]
    b =  [25, 1, 12, -10]

    '''A = [[1, 6, 9],
         [2, 1, 2],
         [3, 6, 9]]
    b =  [1, 2, 3]

    A = [[1, 3, 3],
         [2, 2, 5],
         [3, 2, 6]]
    b = [-2, 7, 12]

    A = [[1, 0, 6, 2],
         [8, 0,-2,-2],
         [2, 9, 1, 3],
         [2, 1,-3, 10]]
    b =  [6,-2,-8, -4]'''
    A_tri, b_tri, c = triangularisationPLREC(A, b)
    if A_tri is not None and b_tri is not None:
        x = remontee(A_tri, b_tri)
        reorder_x_after_column_swaps(x, c)
test()

'''A = [[1, 6, 9],
         [2, 1, 2],
         [3, 6, 9]]
b =  [1,  2, 3]

mat_tri, b_tri, col_perm = triangularisationPLREC(A, b)

x_perm = remontee(mat_tri, b_tri)

x_orig = reorder_x_after_column_swaps(x_perm, col_perm)

print("Solution dans l'ordre original :", x_orig)'''