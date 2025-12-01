from tst2 import *
def afficher_matrice(M):
    for ligne in M:
        print('[', end='')
        for val in ligne:
            print(f'{val:7.4f}', end=' ')
        print(']')
    print()


def copier_matrice(M):
    return [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]

def creer_matrice_identite(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def print_system(mat, b):
    print("Le système est :")
    n = len(mat)
    for i in range(n):
        print(f"[ {' '.join([f'{mat[i][j]:.4f}' for j in range(n)])} ] [ {b[i]:.4f} ]")
    print()

def descente(L, b):
    n = len(b)
    y = [0.0 for _ in range(n)]

    print("--------------- 2- Resoudre Ly = b par descente-----------------")
    print("* le systeme reduit:")
    print_system(L, b)

    print("\n*la resultat donne :")

    for i in range(n):
        somme = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - somme) / L[i][i]
        print(f"y_{i + 1} = {y[i]:2.4f};")

    print()
    return y

def remontee(U, y):
    n = len(y)
    x = [0.0 for _ in range(n)]

    print("--------------- 3- Resoudre Ux =y par remontee-----------------")
    print("* le systeme reduit:")
    print_system(U, y)

    print("\n* la resultat donne :")

    for i in range(n - 1, -1, -1):
        somme = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - somme) / U[i][i]
        print(f"x_{i + 1} = {x[i]:2.4f};")

    print()
    return x

def eliminer_ligne_lu(U, L, k, p):
    n = len(U)
    for i in range(k + 1, n):
        q = U[i][k]
        U[i][k] = 0
        L[i][k] = q / p

        for j in range(k + 1, n):
            U[i][j] = U[i][j] - U[k][j] * (q / p)

