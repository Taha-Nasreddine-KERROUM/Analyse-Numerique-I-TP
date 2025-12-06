from tp1 import *
import time

def substitution(mat, b, x, i_range, j_range):
    for i in i_range:
        somme = 0
        for j in j_range(i):
            somme += mat[i][j] * x[j]
        x[i] = (b[i] - somme) / mat[i][i]
    return x


def copyMat(mat, k, b):
    n = len(mat)
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j == k:
                new[i][j] = b[i]
                continue
            new[i][j] = mat[i][j]

    return new

def copier_matrice(M):
    return [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]

def lireb(n):
    return [float(input(f"b[{i}] = ")) for i in range(n)]

def null_in_diagonal(mat):
    n = len(mat)
    for i in range(n):
        if mat[i][i] == 0:
            return True
    return False


def eliminate(mat, b=None, k=0, pivot=None):
    if pivot == 0:
        print(f"pivot {pivot} = 0")
        raise Exception("pivot nul")

    n = len(mat)
    nb_cols = len(mat[0])

    for i in range(k + 1, n):
        c = mat[i][k] / pivot
        if b is not None:
            b[i] -= c * b[k]
        for j in range(k, nb_cols):
            mat[i][j] -= c * mat[k][j]

def elemenateLUedition(U, L, k, p, n):
    for i in range(k + 1, n):
        q = U[i][k]
        U[i][k] = 0
        L[i][k] = q / p

        for j in range(k + 1, n):
            U[i][j] = U[i][j] - U[k][j] * (q / p)


def elemenateGJedition(augmented, k, n):
    for i in range(n):
        if i != k:
            q = augmented[i][k]
            augmented[i][k] = 0

            for j in range(k + 1, len(augmented[i])):
                augmented[i][j] = augmented[i][j] - q * augmented[k][j]

def descenteITRLUedition (mat, b):
    if isTriangulaireSuprieure(mat) == True:
        print('must be inf')
        return None

    n = len(mat)
    x = [0.0] * n
    x[0] = b[0] / mat[0][0]

    return substitution(
        mat,
        b,
        x,
        i_range=range(1, n),
        j_range=lambda i: range(i)
    )

def print_step_tri(mat, b, k):
    print(f"* Itération K= {k} :")
    print_system(mat, b)

def printX(x):
    for i in range(len(x)):
        print(f"X_{i + 1} = {x[i]:.6f} ;")

def print_step_rem(x):
    print("* La resolution donne :")
    printX(x)
    print()

def afficher_resultat_solution(x):
    print("*la resultat donne :")
    printX(x)

def print_gauss_header(mat, b):
    print("-------------- Gauss ---------------")
    print("* La matrice reduite :")
    print_system(mat, b)

def pivotSearchHelper(mat, k, n):
    p = abs(mat[k][k])
    l = k
    for i in range(k, n):
        if abs(mat[i][k]) > p:
            p = abs(mat[i][k])
            l = i
    return l

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

def apply_pivot_swap(mat, b, col_perm, k, pivot_i, pivot_j):
    if pivot_i != k:
        permet2liner(mat, k, pivot_i)
        b[k], b[pivot_i] = b[pivot_i], b[k]

    if pivot_j != k:
        permet2col(mat, k, pivot_j)
        col_perm[k], col_perm[pivot_j] = col_perm[pivot_j], col_perm[k]

def AfficherX(x, augmented, n):
    for i in range(n):
        x.append(augmented[i][n])

def formMatAug(mat, extra_cols):
    n = len(mat)
    augmented = copier_matrice(mat)

    for j in range(len(extra_cols)):
        for i in range(n):
            augmented[i].append(extra_cols[j][i])

    return augmented


def partieDroite(augmented, n):
    inverse_A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            inverse_A[i][j] = augmented[i][n + j]
    return inverse_A

def normaliserPivot(augmented, pivot, k):
    if pivot == 0:
        raise Exception("pivot nul")

    for j in range(len(augmented[k])):
        augmented[k][j] /= pivot

def print_augmented_matrix(augmented, n):
    for i in range(len(augmented)):
        row = "[ "
        for j in range(len(augmented[i])):
            if j == n:
                row += " | "
            row += f"{augmented[i][j]:8.4f} "
        row += "]"
        print(row)

def sumGauss(mat, n, i, step, x):
    somme = 0
    for j in range(step, n):
        somme = somme + mat[i][j] * x[j]
    return somme

def compute_and_print(i, k, b_i, diag, s1, s2=0, var_name="x"):
    total = b_i - s1 - s2
    x_i = total / diag

    symbolic = f"(b[{i}] - s1 - s2)" if s2 != 0 else f"(b[{i}] - s1)"
    numeric  = f"({b_i:.4f} - {s1:.4f} - {s2:.4f})" if s2 != 0 else f"({b_i:.4f} - {s1:.4f})"

    print(f"{var_name}_{i+1}^({k+1}) = {symbolic} / A[{i}][{i}]")
    print(f"{var_name}_{i+1}^({k+1}) = {numeric} / {diag:.4f}")
    print(f"{var_name}_{i+1}^({k+1}) = {x_i:.6f}")
    print()

    return x_i

def updateXJacobiEdition(mat, n, b, k, x_old, x_new):
    for i in range(n):
        somme = 0

        for j in range(n):
            if j != i:
                somme = somme + mat[i][j] * x_old[j]

        x_new[i] = compute_and_print(i, k, b[i], mat[i][i], somme, 0)
    return x_new

def printX5edition(x, k, n):
    print(f"Resultat iteration {k + 1}:")
    for i in range(n):
        print(f"x_{i + 1}^({k + 1}) = {x[i]:.6f}")
    print()

def convergeEpsilone(x_old, x_new, n, k, epsilon):
    converged = True
    for i in range(n):
        if abs(x_new[i] - x_old[i]) > epsilon:
            converged = False
            break

    if converged:
        print(f"Convergence atteinte a l'iteration {k + 1}")
        return True
    return False

def innerK(mat, n, k, x, b):
    for i in range(n):
        somme_1 = sumGauss(mat, i, i, 0, x)
        somme_2 = sumGauss(mat, n, i, i + 1, x)

        x[i] = compute_and_print(i, k, b[i], mat[i][i], somme_1, somme_2)

def diagonally_dominant(mat):
    n = len(mat)
    for i in range(n):
        diagonal = abs(mat[i][i])

        row_sum = 0
        for j in range(n):
            if i != j:
                row_sum += abs(mat[i][j])

        if diagonal <= row_sum:
            print(f"Error: Matrix is NOT Diagonally Dominant at row {i}.")
            print(f"Diagonal ({diagonal}) <= Sum of neighbors ({row_sum})")
            return False

    print("Matrix is Diagonally Dominant. Convergence is guaranteed.")
    return True

def detp1Choice(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    print("""
    1- recursive
    2- iterative
    """)
    choice = int(input("Choisissez 1,2: "))
    if choice == 1:
        print(f"det|{name}|: ", determinant(A))
    elif choice == 2:
        print(f"det|{name}|: ", determinantIterative(A))

def per2coltp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    col1 = int(input("Entrez la colonne 1: "))
    col2 = int(input("Entrez la colonne 2: "))
    permet2col(A, col1, col2)
    print(f"Après permutation des colonnes {col1} et {col2} de {name}:")
    print_system(A)

def per2linertp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    lin1 = int(input("Entrez la ligne 1: "))
    lin2 = int(input("Entrez la ligne 2: "))
    permet2liner(A, lin1, lin2)
    print(f'Après permutation des lignes {lin1} et {lin2} de {name}:')
    print_system(A)

def symtrqTp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    print(f"{name} est symétrique." if isSymétrique(A) else f"{name} n'est pas symétrique.")

def diagnlTp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
    print(f"{name} est diagonale." if isDiagonale(A) else f"{name} n'est pas diagonale.")

def tringlinfTp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    print(f"{name} est triangulaire inférieure." if isTriangulaireInfrieure(A) else f"{name} n'est pas triangulaire inférieure.")

def tringlsupTp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    print(f"{name} est triangulaire supérieure." if isTriangulaireSuprieure(A) else f"{name} n'est pas triangulaire supérieure.")

def transTp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    print(f"Transposée de {name}:")
    print_system(transpose(A))

def prodTp1(A, B):
    if A is None or B is None:
        print('enterrer deux matrice!')
        return
    print("Produit est A et B:")
    print_system(produit2matrices(A, B))

def sommeTp1(A, B):
    if A is None or B is None:
        print('enterrer deux matrice!')
        return
    print("Somme est:")
    print_system(somme2matrices(A, B))

def affprintTp1(A, name = "A"):
    if A is None:
        print('enterrer une matrice!')
        return
    print(f"Matrice {name}:")
    print_system(A)

def valid(choice, low, high):
    choice = str(choice)
    return choice.isdigit() and low <= int(choice) <= high

def setAb(A, b):
    if A is None:
        print("Entrez la taille de la matrice:")
        n = int(input("n = "))
        A = lireMatrice(n)
    if b is None:
        print("\nEntrez le vecteur b:")
        b = lireb(len(A))
    return A, b