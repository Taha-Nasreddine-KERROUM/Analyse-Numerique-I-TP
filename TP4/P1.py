from helper import *

def decomposition_lu(A):
    n = len(A)
    U = copier_matrice(A)
    L = creer_matrice_identite(n)

    print("--------------- 1- Décomposition -----------------")
    print("*A = L * U\n")

    print(f"* la Matrice U0:")
    afficher_matrice(U)
    print(f"* La Matrice L0:")
    afficher_matrice(L)

    for k in range(n):
        print(f"*** itération k = {k + 1}")
        p = U[k][k]
        print(f"** pivot ={p}")

        eliminer_ligne_lu(U, L, k, p)

        print(f"* la Matrice U{k + 1}:")
        afficher_matrice(U)
        print(f"* La Matrice L{k + 1}:")
        afficher_matrice(L)
        print()

    print("* la Matrice U :")
    afficher_matrice(U)
    print("\n* La Matrice L :")
    afficher_matrice(L)
    print()

    return U, L

def decomposition_lu_recursive(A, k=0, U=None, L=None):
    n = len(A)

    if U is None:
        U = copier_matrice(A)
        L = creer_matrice_identite(n)
        print("--------------- 1- Décomposition (RÉCURSIF) -----------------")
        print("*A = L * U\n")

    if k >= n:
        print("* la Matrice U :")
        afficher_matrice(U)
        print("\n* La Matrice L :")
        afficher_matrice(L)
        print()
        return U, L

    print(f"*** itération k = {k + 1}")
    p = U[k][k]
    print(f"** pivot ={p}")

    eliminer_ligne_lu(U, L, k, p)

    print(f"* la Matrice U{k + 1}:")
    afficher_matrice(U)
    print(f"* La Matrice L{k + 1}:")
    afficher_matrice(L)
    print()

    return decomposition_lu_recursive(A, k + 1, U, L)

def LU(A, b):
    print_system(A, b)

    U, L = decomposition_lu(A)

    y = descente(L, b)

    x = remontee(U, y)

    return x


A2 = [[4, 8, 12],
      [3, 8, 13],
      [2, 9, 18]]

b2 = [4, 5, 11]

x2 = LU(A2, b2)