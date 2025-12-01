from tp3p3 import *

def decomposition_LU(mat, b):
    n = len(mat)

    U = copier_matrice(mat)
    L = matriceDidentit(n)

    print_system(mat, b)
    print("------------ 1- Decomposition ---------------")
    print()
    print("*A = L * U")
    print()

    print("la Matrice U0:")
    print_system(U)
    print("La Matrice L0:")
    print_system(L)

    for k in range(n - 1):
        print(f"** iteration k = {k + 1}")

        p = U[k][k]
        print(f"** pivot ={p}")

        if p == 0:
            raise Exception("pivot nul")

        elemenateLUedition(U, L, k, p, n)

        print(f"* la Matrice U{k + 1}:")
        print_system(U)
        print(f"* La Matrice L{k + 1}:")
        print_system(L)

    print("la Matrice U :")
    print_system(U)
    print("La Matrice L :")
    print_system(L)

    return L, U

def decomposition_LU_REC(mat, b, k=0, U=None, L=None, first_call=True):
    n = len(mat)

    if U is None:
        U = copier_matrice(mat)
    if L is None:
        L = matriceDidentit(n)

    if first_call:
        print_system(mat, b)
        print("------------ 1- Decomposition ---------------")
        print()
        print("*A = L * U")
        print()
        print("la Matrice U0:")
        print_system(U)
        print("La Matrice L0:")
        print_system(L)

    if k >= n - 1:
        print("la Matrice U :")
        print_system(U)
        print("La Matrice L :")
        print_system(L)
        return L, U

    print(f"** iteration k = {k + 1}")
    p = U[k][k]
    print(f"** pivot ={p}")

    if p == 0:
        raise Exception("pivot nul")

    elemenateLUedition(U, L, k, p, n)

    print(f"* la Matrice U{k + 1}:")
    print_system(U)
    print(f"* La Matrice L{k + 1}:")
    print_system(L)

    return decomposition_LU_REC(mat, b, k + 1, U, L, False)


def solve_LU(mat, b):
    L, U = decomposition_LU(mat, b)

    print("------------ 2- Resoudre Ly = b par descente-----------------")
    print()
    print("le systeme reduit:")
    print_system(L, b)

    y = descenteITRLUedition(L, b)

    print("*la resultat donne :")
    printX(y)
    print()

    print("------------ 3- Resoudre Ux =y par remontee-----------------")
    print()
    print("le systeme reduit:")
    print_system(U, y)

    x = remontéeITR(U, y)

    print("la resultat donne :")
    printX(x)

    return x


def solve_LU_REC(mat, b):
    L, U = decomposition_LU_REC(mat, b)

    print("------------ 2- Resoudre Ly = b par descente-----------------")
    print()
    print("le systeme reduit:")
    print_system(L, b)

    y = descenteREC(L, b)

    print("*la resultat donne :")
    printX(y)
    print()

    print("------------ 3- Resoudre Ux =y par remontee-----------------")
    print()
    print("le systeme reduit:")
    print_system(U, y)

    x = remontéeREC(U, y)

    print("la resultat donne :")
    printX(x)

    return x