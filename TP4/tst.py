def afficher_matrice(M):
    print("[ ", end="")
    for i, ligne in enumerate(M):
        if i > 0:
            print("  ", end="")
        print("[", end="")
        print(" ".join(f"{val:7.4f}" for val in ligne), end="")
        print(" ]")
        if i < len(M) - 1:
            print("  ", end="")
    print("]")


def afficher_systeme(M, b):
    print("Le système est :")
    n = len(M)
    for i in range(n):
        print(f"[ {' '.join([f'{M[i][j]:.4f}' for j in range(n)])} ] [ {b[i]:.4f} ]")
    print()


def afficher_matrice_augmentee(M, n):
    print("[ ", end="")
    for i in range(len(M)):
        if i > 0:
            print("  ", end="")
        print("[", end="")
        for j in range(len(M[i])):
            if j == n:
                print(" ] [ ", end="")
            print(f"{M[i][j]:7.4f}", end="")
            if j < len(M[i]) - 1 and j != n - 1:
                print(" ", end="")
        print(" ]")
        if i < len(M) - 1:
            print("  ", end="")
    print("]")


def afficher_matrice_augmentee_inverse(M, n):
    afficher_matrice_augmentee(M, n)


def afficher_resultat_solution(x):
    print("*la resultat donne :")
    for i in range(len(x)):
        print(f"x_{i + 1} = {x[i]:.4f};")


# ============== HELPER FUNCTIONS ==============

def copier_matrice(M):
    return [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]


def creer_matrice_identite(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def former_matrice_augmentee(A, b_ou_I):
    n = len(A)

    if isinstance(b_ou_I[0], (int, float)):
        return [[A[i][j] for j in range(n)] + [b_ou_I[i]] for i in range(n)]
    else:
        return [[A[i][j] for j in range(n)] + [b_ou_I[i][k] for k in range(n)] for i in range(n)]


def normaliser_pivot(matrice, k, nb_cols):
    pivot = matrice[k][k]
    for j in range(nb_cols):
        matrice[k][j] = matrice[k][j] / pivot
    return pivot


def eliminer_autres_lignes(matrice, k, nb_cols, debut_col=0):
    n = len(matrice)
    for i in range(n):
        if i != k:
            q = matrice[i][k]
            for j in range(debut_col, nb_cols):
                matrice[i][j] = matrice[i][j] - q * matrice[k][j]


def extraire_solution(matrice_aug, n):
    return [matrice_aug[i][n] for i in range(n)]


def extraire_inverse(matrice_aug, n):
    return [[matrice_aug[i][j + n] for j in range(n)] for i in range(n)]


def multiplier_matrices(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)] for i in range(n)]


def decomposition_lu(A):
    n = len(A)
    U = copier_matrice(A)
    L = creer_matrice_identite(n)

    print("--------------- 1- Décomposition -----------------")
    print("*A = L * U\n")

    for k in range(n):
        print(f"*** itération k = {k + 1}")
        p = U[k][k]
        print(f"** pivot ={p}")

        for i in range(k + 1, n):
            q = U[i][k]
            U[i][k] = 0
            L[i][k] = q / p

            for j in range(k + 1, n):
                U[i][j] = U[i][j] - U[k][j] * (q / p)

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


def descente(L, b):
    n = len(b)
    y = [0.0 for _ in range(n)]

    print("--------------- 2- Resoudre Ly = b par descente-----------------")
    print("* le systeme reduit:")
    afficher_systeme(L, b)
    print("\n*la resultat donne :")

    for i in range(n):
        somme = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - somme) / L[i][i]
        print(f"y_{i + 1} = {y[i]:.4f};")

    print()
    return y


def remontee(U, y):
    n = len(y)
    x = [0.0 for _ in range(n)]

    print("--------------- 3- Resoudre Ux =y par remontee-----------------")
    print("* le systeme reduit:")
    afficher_systeme(U, y)
    print("\n* la resultat donne :")

    for i in range(n - 1, -1, -1):
        somme = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - somme) / U[i][i]
        print(f"x_{i + 1} = {x[i]:.4f};")

    print()
    return x


def resoudre_systeme(A, b):
    print("Le systeme est :")
    afficher_systeme(A, b)

    U, L = decomposition_lu(A)

    y = descente(L, b)

    x = remontee(U, y)

    return x


# ============== VERSIONS RÉCURSIVES ==============

def descente_recursive(L, b, i=0, y=None):
    n = len(b)

    if y is None:
        y = [0.0 for _ in range(n)]
        print("--------------- 2- Resoudre Ly = b par descente (RÉCURSIF) -----------------")
        print("* le systeme reduit:")
        afficher_systeme(L, b)
        print("\n*la resultat donne :")

    if i >= n:
        print()
        return y

    somme = sum(L[i][j] * y[j] for j in range(i))
    y[i] = (b[i] - somme) / L[i][i]
    print(f"y_{i + 1} = {y[i]:.4f};")

    return descente_recursive(L, b, i + 1, y)


def remontee_recursive(U, y, i=None, x=None):
    n = len(y)

    if x is None:
        x = [0.0 for _ in range(n)]
        i = n - 1
        print("--------------- 3- Resoudre Ux =y par remontee (RÉCURSIF) -----------------")
        print("* le systeme reduit:")
        afficher_systeme(U, y)
        print("\n* la resultat donne :")

    if i < 0:
        print()
        return x

    somme = sum(U[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (y[i] - somme) / U[i][i]
    print(f"x_{i + 1} = {x[i]:.4f};")

    return remontee_recursive(U, y, i - 1, x)


def resoudre_systeme_recursif(A, b):
    print("Le systeme est :")
    afficher_systeme(A, b)

    U, L = decomposition_lu(A)

    y = descente_recursive(L, b)

    x = remontee_recursive(U, y)

    return x


# ============== PARTIE 2: ALGORITHME DE GAUSS-JORDAN ==============

def gauss_jordan_systeme(A, b):
    n = len(A)

    matrice_aug = former_matrice_augmentee(A, b)

    print("Le systeme est :")
    afficher_matrice_augmentee(matrice_aug, n)
    print("\n--------------- Résolution par Gauss-Jordan -----------------\n")

    for k in range(n):
        print(f"*** Itération k = {k + 1}")

        pivot = normaliser_pivot(matrice_aug, k, n + 1)
        print(f"** pivot = {pivot}")

        print(f"* Après normalisation:")
        afficher_matrice_augmentee(matrice_aug, n)

        eliminer_autres_lignes(matrice_aug, k, n + 1)

        print(f"* Après élimination:")
        afficher_matrice_augmentee(matrice_aug, n)
        print()

    print("// Afficher le vecteur solution X")
    x = extraire_solution(matrice_aug, n)
    afficher_resultat_solution(x)

    return x


def gauss_jordan_inverse(A):
    n = len(A)

    I = creer_matrice_identite(n)
    matrice_aug = former_matrice_augmentee(A, I)

    print("La matrice A :")
    afficher_matrice(A)
    print("\n// Former la matrice augmentée [A | I]")
    afficher_matrice_augmentee_inverse(matrice_aug, n)
    print("\n--------------- Calcul de l'inverse par Gauss-Jordan -----------------\n")

    # Pour k = 1 à n
    for k in range(n):
        print(f"*** Itération k = {k + 1}")

        pivot = normaliser_pivot(matrice_aug, k, 2 * n)
        print(f"** pivot = {pivot}")

        print(f"* Après normalisation:")
        afficher_matrice_augmentee_inverse(matrice_aug, n)

        eliminer_autres_lignes(matrice_aug, k, 2 * n)

        print(f"* Après élimination:")
        afficher_matrice_augmentee_inverse(matrice_aug, n)
        print()

    A_inv = extraire_inverse(matrice_aug, n)

    print("// La partie droite de la matrice contient A^(-1)")
    print("* La matrice inverse A^(-1) :")
    afficher_matrice(A_inv)

    return A_inv


def afficher_matrice_augmentee(M, n):
    print("[ ", end="")
    for i in range(len(M)):
        if i > 0:
            print("  ", end="")
        print("[", end="")
        for j in range(len(M[i])):
            if j == n:
                print(" ] [ ", end="")
            print(f"{M[i][j]:7.4f}", end="")
            if j < len(M[i]) - 1 and j != n - 1:
                print(" ", end="")
        print(" ]")
        if i < len(M) - 1:
            print("  ", end="")
    print("]")


def afficher_matrice_augmentee_inverse(M, n):
    print("[ ", end="")
    for i in range(len(M)):
        if i > 0:
            print("  ", end="")
        print("[", end="")
        for j in range(len(M[i])):
            if j == n:
                print(" ] [ ", end="")
            print(f"{M[i][j]:7.4f}", end="")
            if j < len(M[i]) - 1 and j != n - 1:
                print(" ", end="")
        print(" ]")
        if i < len(M) - 1:
            print("  ", end="")
    print("]")


# ============== VERSIONS RÉCURSIVES GAUSS-JORDAN ==============

def normaliser_ligne_recursive(ligne, pivot, j=0):
    if j >= len(ligne):
        return

    ligne[j] = ligne[j] / pivot
    normaliser_ligne_recursive(ligne, pivot, j + 1)


def eliminer_colonne_recursive(matrice_aug, k, pivot_row, i=0):
    n = len(matrice_aug)

    if i >= n:
        return

    if i != k:
        q = matrice_aug[i][k]
        eliminer_ligne_recursive(matrice_aug[i], pivot_row, q, 0)

    eliminer_colonne_recursive(matrice_aug, k, pivot_row, i + 1)


def eliminer_ligne_recursive(ligne, pivot_row, q, j=0):
    if j >= len(ligne):
        return

    ligne[j] = ligne[j] - q * pivot_row[j]
    eliminer_ligne_recursive(ligne, pivot_row, q, j + 1)


def gauss_jordan_systeme_recursive(A, b, k=0, matrice_aug=None):
    n = len(A)

    if matrice_aug is None:
        matrice_aug = former_matrice_augmentee(A, b)
        print("Le systeme est :")
        afficher_matrice_augmentee(matrice_aug, n)
        print("\n--------------- Résolution par Gauss-Jordan (RÉCURSIF) -----------------\n")

    if k >= n:
        print("// Afficher le vecteur solution X")
        x = extraire_solution(matrice_aug, n)
        afficher_resultat_solution(x)
        return x

    print(f"*** Itération k = {k + 1}")

    pivot = normaliser_pivot(matrice_aug, k, n + 1)
    print(f"** pivot = {pivot}")

    print(f"* Après normalisation:")
    afficher_matrice_augmentee(matrice_aug, n)

    eliminer_autres_lignes(matrice_aug, k, n + 1)

    print(f"* Après élimination:")
    afficher_matrice_augmentee(matrice_aug, n)
    print()

    return gauss_jordan_systeme_recursive(A, b, k + 1, matrice_aug)


def gauss_jordan_inverse_recursive(A, k=0, matrice_aug=None):
    n = len(A)

    if matrice_aug is None:
        I = creer_matrice_identite(n)
        matrice_aug = former_matrice_augmentee(A, I)
        print("La matrice A :")
        afficher_matrice(A)
        print("\n// Former la matrice augmentée [A | I]")
        afficher_matrice_augmentee_inverse(matrice_aug, n)
        print("\n--------------- Calcul de l'inverse par Gauss-Jordan (RÉCURSIF) -----------------\n")

    if k >= n:
        A_inv = extraire_inverse(matrice_aug, n)
        print("// La partie droite de la matrice contient A^(-1)")
        print("* La matrice inverse A^(-1) :")
        afficher_matrice(A_inv)
        return A_inv

    print(f"*** Itération k = {k + 1}")

    pivot = normaliser_pivot(matrice_aug, k, 2 * n)
    print(f"** pivot = {pivot}")

    print(f"* Après normalisation:")
    afficher_matrice_augmentee_inverse(matrice_aug, n)

    eliminer_autres_lignes(matrice_aug, k, 2 * n)

    print(f"* Après élimination:")
    afficher_matrice_augmentee_inverse(matrice_aug, n)
    print()

    return gauss_jordan_inverse_recursive(A, k + 1, matrice_aug)

#
# # Exemple 1
# print("=" * 60)
# print("EXEMPLE 1: VERSION ITÉRATIVE")
# print("=" * 60)
# A1 = [[1, 2, 3],
#       [1, 1, 2],
#       [1, 1, 1]]
#
# b1 = [2, 0, 1]
#
# x1 = resoudre_systeme(A1, b1)


# Exemple 2
print("\n\n" + "=" * 60)
print("EXEMPLE 2: VERSION ITÉRATIVE")
print("=" * 60)
A2 = [[4, 8, 12],
      [3, 8, 13],
      [2, 9, 18]]

b2 = [4, 5, 11]

x2 = resoudre_systeme(A2, b2)
#
# print("\n" + "=" * 60)
# print("Solution finale:")
# print(f"x = {[round(val, 4) for val in x2]}")
# print("=" * 60)
#
# # ============== EXEMPLES AVEC VERSION RÉCURSIVE ==============
#
# # Exemple 1 - Version Récursive
# print("\n\n" + "=" * 60)
# print("EXEMPLE 1: VERSION RÉCURSIVE")
# print("=" * 60)
# A1_rec = [[1, 2, 3],
#           [1, 1, 2],
#           [1, 1, 1]]
#
# b1_rec = [2, 0, 1]
#
# x1_rec = resoudre_systeme_recursif(A1_rec, b1_rec)
#
# print("\n" + "=" * 60)
# print("Solution finale:")
# print(f"x = {[round(val, 4) for val in x1_rec]}")
# print("=" * 60)
#
# # Exemple 2 - Version Récursive
# print("\n\n" + "=" * 60)
# print("EXEMPLE 2: VERSION RÉCURSIVE")
# print("=" * 60)
# A2_rec = [[4, 8, 12],
#           [3, 8, 13],
#           [2, 9, 18]]
#
# b2_rec = [4, 5, 11]
#
# x2_rec = resoudre_systeme_recursif(A2_rec, b2_rec)
#
# print("\n" + "=" * 60)
# print("Solution finale:")
# print(f"x = {[round(val, 4) for val in x2_rec]}")
# print("=" * 60)
#
# # ============== PARTIE 2: EXEMPLES GAUSS-JORDAN ==============
#
# # Exemple 1 - Gauss-Jordan pour résoudre un système
# print("\n\n" + "=" * 60)
# print("PARTIE 2 - EXEMPLE 1: GAUSS-JORDAN - RÉSOLUTION SYSTÈME")
# print("=" * 60)
# A_gj1 = [[1, 2, 3],
#          [1, 1, 2],
#          [1, 1, 1]]
#
# b_gj1 = [2, 0, 1]
#
# x_gj1 = gauss_jordan_systeme(A_gj1, b_gj1)
#
# print("\n" + "=" * 60)
# print("Solution finale:")
# print(f"x = {[round(val, 4) for val in x_gj1]}")
# print("=" * 60)
#
# # Exemple 2 - Gauss-Jordan pour calculer l'inverse
# print("\n\n" + "=" * 60)
# print("PARTIE 2 - EXEMPLE 2: GAUSS-JORDAN - CALCUL DE L'INVERSE")
# print("=" * 60)
# A_gj2 = [[1, 2, 3],
#          [1, 1, 2],
#          [1, 1, 1]]
#
# A_inv = gauss_jordan_inverse(A_gj2)
#
# print("\n" + "=" * 60)
# print("Matrice inverse A^(-1) finale:")
# print("=" * 60)
# afficher_matrice(A_inv)
#
# # Vérification: A * A^(-1) = I
# print("\n// Vérification: A * A^(-1) = I")
# verification = multiplier_matrices(A_gj2, A_inv)
# afficher_matrice(verification)
#
# # ============== PARTIE 2: EXEMPLES GAUSS-JORDAN RÉCURSIF ==============
#
# # Exemple 1 - Gauss-Jordan récursif pour résoudre un système
# print("\n\n" + "=" * 60)
# print("PARTIE 2 - EXEMPLE 1: GAUSS-JORDAN RÉCURSIF - RÉSOLUTION SYSTÈME")
# print("=" * 60)
# A_gj_rec1 = [[1, 2, 3],
#              [1, 1, 2],
#              [1, 1, 1]]
#
# b_gj_rec1 = [2, 0, 1]
#
# x_gj_rec1 = gauss_jordan_systeme_recursive(A_gj_rec1, b_gj_rec1)
#
# print("\n" + "=" * 60)
# print("Solution finale:")
# print(f"x = {[round(val, 4) for val in x_gj_rec1]}")
# print("=" * 60)
#
# # Exemple 2 - Gauss-Jordan récursif pour calculer l'inverse
# print("\n\n" + "=" * 60)
# print("PARTIE 2 - EXEMPLE 2: GAUSS-JORDAN RÉCURSIF - CALCUL DE L'INVERSE")
# print("=" * 60)
# A_gj_rec2 = [[1, 2, 3],
#              [1, 1, 2],
#              [1, 1, 1]]
#
# A_inv_rec = gauss_jordan_inverse_recursive(A_gj_rec2)
#
# print("\n" + "=" * 60)
# print("Matrice inverse A^(-1) finale:")
# print("=" * 60)
# afficher_matrice(A_inv_rec)
#
# # Vérification: A * A^(-1) = I
# print("\n// Vérification: A * A^(-1) = I")
# verification_rec = multiplier_matrices(A_gj_rec2, A_inv_rec)
# afficher_matrice(verification_rec)