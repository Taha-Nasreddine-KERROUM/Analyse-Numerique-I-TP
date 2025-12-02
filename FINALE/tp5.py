from tp4p2 import *

def jacobi(mat, b, n_max, epsilon=1e-6):
    if not diagonally_dominant(mat):
        print("WARNING: The matrix is not diagonally dominant.")
        print("The algorithm will likely diverge (result in infinity).")

    n = len(mat)

    x_old = [0.0] * n
    x_new = [0.0] * n

    print(f"Initialisation: x^(0) = {x_old}")
    print()

    for k in range(n_max):
        print(f"---------- Iteration k = {k + 1} ----------")

        x_new = updateXJacobiEdition(mat, n, b, k, x_old, x_new)

        printX5edition(x_new, k, n)

        if convergeEpsilone(x_old, x_new, n, k, epsilon):
            break

        x_old = x_new[:]

    print("\n")
    print("Solution finale:")
    printX(x_new)

    return x_new

def innerK(mat, n, k, x, b):
    for i in range(n):
        somme_1 = sumGauss(mat, i, i, 0, x)
        somme_2 = sumGauss(mat, n, i, i + 1, x)

        x[i] = compute_and_print(i, k, b[i], mat[i][i], somme_1, somme_2)

def gauss_seidel(mat, b, n_max, epsilon=1e-6):
    n = len(mat)

    x = [0.0] * n
    x_old = [0.0] * n

    print(f"Initialisation: x^(0) = {x}")
    print()

    for k in range(n_max):
        print(f"---------- Iteration k = {k} ----------")

        x_old = x[:]

        innerK(mat, n, k, x, b)

        printX5edition(x, k, n)

        if convergeEpsilone(x_old, x, n, k, epsilon):
            break

    print("\n")
    print("Solution finale:")
    printX(x)

    return x


def jacobi_REC(mat, b, n_max, epsilon=1e-6, k=0, x_old=None, x_new=None):
    n = len(mat)

    if x_old is None:
        if not diagonally_dominant(mat):
            print("WARNING: The matrix is not diagonally dominant.")
            print("The algorithm will likely diverge (result in infinity).")

        x_old = [0.0] * n
        x_new = [0.0] * n
        print(f"Initialisation: x^(0) = {x_old}")
        print()

    if k >= n_max:
        print("\n")
        print("Solution finale:")
        printX(x_new if k > 0 else x_old)
        return x_new if k > 0 else x_old

    print(f"---------- Iteration k = {k + 1} ----------")

    x_new = updateXJacobiEdition(mat, n, b, k, x_old, x_new)

    printX5edition(x_new, k, n)

    if convergeEpsilone(x_old, x_new, n, k, epsilon):
        print("\n")
        print("Solution finale:")
        printX(x_new)
        return x_new

    return jacobi_REC(mat, b, n_max, epsilon, k + 1, x_new[:], [0.0] * n)

def gauss_seidel_REC(mat, b, n_max, epsilon=1e-6, k=0, x=None, x_old=None):
    n = len(mat)

    if x is None:
        x = [0.0] * n
        x_old = [0.0] * n
        print(f"Initialisation: x^(0) = {x}")
        print()

    if k >= n_max:
        print("\n")
        print("Solution finale:")
        printX(x)
        return x

    if k > 0:
        if convergeEpsilone(x_old, x, n, k, epsilon):
            print(f"Convergence atteinte a l'iteration {k}")
            print("\n")
            print("Solution finale:")
            printX(x)
            return x

    print(f"---------- Iteration k = {k} ----------")

    x_old = x[:]

    innerK(mat, n, k, x, b)

    printX5edition(x, k, n)

    return gauss_seidel_REC(mat, b, n_max, epsilon, k + 1, x, x_old)