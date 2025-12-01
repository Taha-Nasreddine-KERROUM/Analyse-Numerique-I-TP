def afficher_matrice(M):
    """Affiche une matrice de manière formatée"""
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
    """Affiche un système matriciel M * x = b"""
    print("[ ", end="")
    for i, ligne in enumerate(M):
        if i > 0:
            print("  ", end="")
        print("[", end="")
        print(" ".join(f"{val:7.4f}" for val in ligne), end="")
        print(" ] ", end="")
        if i == len(M) // 2:
            print("[ ", end="")
        else:
            print("  ", end="")
        print(f"{b[i]:7.4f} ]")
        if i < len(M) - 1:
            print("  ", end="")
    print("]")


def afficher_matrice_augmentee(M, n):
    """Affiche une matrice augmentée [A | b]"""
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
    """Affiche une matrice augmentée [A | I]"""
    afficher_matrice_augmentee(M, n)  # Même format


def afficher_resultat_solution(x):
    """Affiche le vecteur solution"""
    print("*la resultat donne :")
    for i in range(len(x)):
        print(f"x_{i + 1} = {x[i]:.4f};")


# ============== HELPER FUNCTIONS ==============

def copier_matrice(M):
    return [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]


def creer_matrice_identite(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def former_matrice_augmentee(A, b):
    n = len(A)

    return [[A[i][j] for j in range(n)] + [b[i]] for i in range(n)]


def normaliser_pivot(matrice, k, n):
    pivot = matrice[k][k]
    for j in range(n):
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
    """
    Extrait le vecteur solution de la dernière colonne de la matrice augmentée

    Paramètres:
        matrice_aug: matrice augmentée après Gauss-Jordan
        n: taille du système

    Retourne:
        x: vecteur solution
    """
    return [matrice_aug[i][n] for i in range(n)]


def extraire_inverse(matrice_aug, n):
    """
    Extrait la matrice inverse de la partie droite de [A | I]

    Paramètres:
        matrice_aug: matrice augmentée après Gauss-Jordan
        n: taille de la matrice

    Retourne:
        A_inv: matrice inverse
    """
    return [[matrice_aug[i][j + n] for j in range(n)] for i in range(n)]


def multiplier_matrices(A, B):
    """
    Multiplie deux matrices A et B

    Paramètres:
        A: première matrice
        B: deuxième matrice

    Retourne:
        C = A * B
    """
    n = len(A)
    m = len(B[0])
    p = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)] for i in range(n)]


def decomposition_lu(A):
    """
    Décompose la matrice A en produit LU
    où L est triangulaire inférieure et U est triangulaire supérieure

    Données: A = (A[i,j]), n le nombre de lignes et colonnes
    Retourne: U (triangulaire supérieure), L (triangulaire inférieure)
    """
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


def eliminer_ligne_lu(U, L, k, i, p):
    q = U[i][k]
    U[i][k] = 0
    L[i][k] = q / p

    for j in range(k + 1, len(U)):
        U[i][j] = U[i][j] - U[k][j] * (q / p)


def eliminer_colonne_lu_recursive(U, L, k, p, i):
    n = len(U)

    if i >= n:
        return

    eliminer_ligne_lu(U, L, k, i, p)
    eliminer_colonne_lu_recursive(U, L, k, p, i + 1)


def decomposition_lu_recursive(A, k=0, U=None, L=None):
    """
    Décompose la matrice A en produit LU (version récursive)

    Paramètres:
        A: matrice à décomposer
        k: indice de l'itération courante
        U: matrice triangulaire supérieure
        L: matrice triangulaire inférieure

    Retourne: U, L
    """
    n = len(A)

    # Initialisation
    if U is None:
        U = copier_matrice(A)
        L = creer_matrice_identite(n)
        print("--------------- 1- Décomposition (RÉCURSIF) -----------------")
        print("*A = L * U\n")

    # Cas de base: toutes les itérations sont terminées
    if k >= n:
        print("* la Matrice U :")
        afficher_matrice(U)
        print("\n* La Matrice L :")
        afficher_matrice(L)
        print()
        return U, L

    # Itération k
    print(f"*** itération k = {k + 1}")
    p = U[k][k]
    print(f"** pivot ={p}")

    # Éliminer la colonne k pour toutes les lignes en dessous
    eliminer_colonne_lu_recursive(U, L, k, p, k + 1)

    print(f"* la Matrice U{k + 1}:")
    afficher_matrice(U)
    print(f"* La Matrice L{k + 1}:")
    afficher_matrice(L)
    print()

    # Appel récursif pour l'itération suivante
    return decomposition_lu_recursive(A, k + 1, U, L)


def descente(L, b):
    """
    Résout le système Ly = b par l'algorithme de la descente
    où L est une matrice triangulaire inférieure

    Retourne: y le vecteur solution
    """
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
    """
    Résout le système Ux = y par l'algorithme de la remontée
    où U est une matrice triangulaire supérieure

    Retourne: x le vecteur solution
    """
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
    """
    Résout le système linéaire Ax = b en utilisant la décomposition LU

    Paramètres:
        A: matrice des coefficients
        b: vecteur second membre

    Retourne:
        x: vecteur solution
    """
    print("Le systeme est :")
    afficher_systeme(A, b)

    # 1. Décomposition LU
    U, L = decomposition_lu(A)

    # 2. Résoudre Ly = b par descente
    y = descente(L, b)

    # 3. Résoudre Ux = y par remontée
    x = remontee(U, y)

    return x


# ============== VERSIONS RÉCURSIVES ==============

def descente_recursive(L, b, i=0, y=None):
    """
    Résout le système Ly = b par l'algorithme de la descente (version récursive)

    Paramètres:
        L: matrice triangulaire inférieure
        b: vecteur second membre
        i: indice courant (pour la récursion)
        y: vecteur solution en construction

    Retourne: y le vecteur solution
    """
    n = len(b)

    # Initialisation
    if y is None:
        y = [0.0 for _ in range(n)]
        print("--------------- 2- Resoudre Ly = b par descente (RÉCURSIF) -----------------")
        print("* le systeme reduit:")
        afficher_systeme(L, b)
        print("\n*la resultat donne :")

    # Cas de base: tous les éléments sont calculés
    if i >= n:
        print()
        return y

    # Calcul récursif
    somme = sum(L[i][j] * y[j] for j in range(i))
    y[i] = (b[i] - somme) / L[i][i]
    print(f"y_{i + 1} = {y[i]:.4f};")

    # Appel récursif pour l'élément suivant
    return descente_recursive(L, b, i + 1, y)


def remontee_recursive(U, y, i=None, x=None):
    """
    Résout le système Ux = y par l'algorithme de la remontée (version récursive)

    Paramètres:
        U: matrice triangulaire supérieure
        y: vecteur second membre
        i: indice courant (pour la récursion)
        x: vecteur solution en construction

    Retourne: x le vecteur solution
    """
    n = len(y)

    # Initialisation
    if x is None:
        x = [0.0 for _ in range(n)]
        i = n - 1
        print("--------------- 3- Resoudre Ux =y par remontee (RÉCURSIF) -----------------")
        print("* le systeme reduit:")
        afficher_systeme(U, y)
        print("\n* la resultat donne :")

    # Cas de base: tous les éléments sont calculés
    if i < 0:
        print()
        return x

    # Calcul récursif
    somme = sum(U[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (y[i] - somme) / U[i][i]
    print(f"x_{i + 1} = {x[i]:.4f};")

    # Appel récursif pour l'élément précédent
    return remontee_recursive(U, y, i - 1, x)


def resoudre_systeme_recursif(A, b):
    """
    Résout le système linéaire Ax = b en utilisant la décomposition LU
    avec descente et remontée récursives

    Paramètres:
        A: matrice des coefficients
        b: vecteur second membre

    Retourne:
        x: vecteur solution
    """
    print("Le systeme est :")
    afficher_systeme(A, b)

    # 1. Décomposition LU récursive
    U, L = decomposition_lu_recursive(A)

    # 2. Résoudre Ly = b par descente récursive
    y = descente_recursive(L, b)

    # 3. Résoudre Ux = y par remontée récursive
    x = remontee_recursive(U, y)

    return x


# ============== PARTIE 2: ALGORITHME DE GAUSS-JORDAN ==============

def gauss_jordan_systeme(A, b):
    """
    Résout le système linéaire Ax = b par la méthode de Gauss-Jordan

    Paramètres:
        A: matrice des coefficients (n x n)
        b: vecteur second membre (n)

    Retourne:
        x: vecteur solution
    """
    n = len(A)

    # Former la matrice augmentée [A | b]
    matrice_aug = former_matrice_augmentee(A, b)

    print("Le systeme est :")
    afficher_matrice_augmentee(matrice_aug, n)
    print("\n--------------- Résolution par Gauss-Jordan -----------------\n")

    # Pour k = 1 à n
    for k in range(n):
        print(f"*** Itération k = {k + 1}")

        # Normalisation du pivot
        pivot = normaliser_pivot(matrice_aug, k, n + 1)
        print(f"** pivot = {pivot}")

        print(f"* Après normalisation:")
        afficher_matrice_augmentee(matrice_aug, n)

        # Mise à zéro des autres lignes
        eliminer_autres_lignes(matrice_aug, k, n + 1)

        print(f"* Après élimination:")
        afficher_matrice_augmentee(matrice_aug, n)
        print()

    # Afficher le vecteur solution
    print("// Afficher le vecteur solution X")
    x = extraire_solution(matrice_aug, n)
    afficher_resultat_solution(x)

    return x


def gauss_jordan_inverse(A):
    """
    Calcule la matrice inverse A^(-1) par la méthode de Gauss-Jordan

    Paramètres:
        A: matrice carrée (n x n)

    Retourne:
        A_inv: matrice inverse
    """
    n = len(A)

    # Former la matrice augmentée [A | I]
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

        # Normalisation du pivot
        pivot = normaliser_pivot(matrice_aug, k, 2 * n)
        print(f"** pivot = {pivot}")

        print(f"* Après normalisation:")
        afficher_matrice_augmentee_inverse(matrice_aug, n)

        # Mise à zéro des autres lignes
        eliminer_autres_lignes(matrice_aug, k, 2 * n)

        print(f"* Après élimination:")
        afficher_matrice_augmentee_inverse(matrice_aug, n)
        print()

    # Extraire la matrice inverse (partie droite de [A | I])
    A_inv = extraire_inverse(matrice_aug, n)

    print("// La partie droite de la matrice contient A^(-1)")
    print("* La matrice inverse A^(-1) :")
    afficher_matrice(A_inv)

    return A_inv


def afficher_matrice_augmentee(M, n):
    """Affiche une matrice augmentée [A | b]"""
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
    """Affiche une matrice augmentée [A | I]"""
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
    """
    Normalise une ligne récursivement en divisant par le pivot

    Paramètres:
        ligne: la ligne à normaliser
        pivot: le pivot
        j: indice courant (pour la récursion)
    """
    if j >= len(ligne):
        return

    ligne[j] = ligne[j] / pivot
    normaliser_ligne_recursive(ligne, pivot, j + 1)


def eliminer_colonne_recursive(matrice_aug, k, pivot_row, i=0):
    """
    Élimine la colonne k pour toutes les lignes sauf k (récursif)

    Paramètres:
        matrice_aug: matrice augmentée
        k: indice de la colonne pivot
        pivot_row: la ligne du pivot (déjà normalisée)
        i: indice de ligne courant
    """
    n = len(matrice_aug)

    if i >= n:
        return

    if i != k:
        q = matrice_aug[i][k]
        eliminer_ligne_recursive(matrice_aug[i], pivot_row, q, 0)

    eliminer_colonne_recursive(matrice_aug, k, pivot_row, i + 1)


def eliminer_ligne_recursive(ligne, pivot_row, q, j=0):
    """
    Élimine un élément d'une ligne récursivement

    Paramètres:
        ligne: la ligne à modifier
        pivot_row: la ligne du pivot
        q: le multiplicateur
        j: indice courant
    """
    if j >= len(ligne):
        return

    ligne[j] = ligne[j] - q * pivot_row[j]
    eliminer_ligne_recursive(ligne, pivot_row, q, j + 1)


def gauss_jordan_systeme_recursive(A, b, k=0, matrice_aug=None):
    """
    Résout le système linéaire Ax = b par Gauss-Jordan (version récursive)

    Paramètres:
        A: matrice des coefficients
        b: vecteur second membre
        k: indice de l'itération courante
        matrice_aug: matrice augmentée [A | b]

    Retourne:
        x: vecteur solution
    """
    n = len(A)

    # Initialisation
    if matrice_aug is None:
        matrice_aug = former_matrice_augmentee(A, b)
        print("Le systeme est :")
        afficher_matrice_augmentee(matrice_aug, n)
        print("\n--------------- Résolution par Gauss-Jordan (RÉCURSIF) -----------------\n")

    # Cas de base: toutes les itérations sont terminées
    if k >= n:
        print("// Afficher le vecteur solution X")
        x = extraire_solution(matrice_aug, n)
        afficher_resultat_solution(x)
        return x

    # Itération k
    print(f"*** Itération k = {k + 1}")

    # Normalisation du pivot
    pivot = normaliser_pivot(matrice_aug, k, n + 1)
    print(f"** pivot = {pivot}")

    print(f"* Après normalisation:")
    afficher_matrice_augmentee(matrice_aug, n)

    # Mise à zéro des autres lignes
    eliminer_autres_lignes(matrice_aug, k, n + 1)

    print(f"* Après élimination:")
    afficher_matrice_augmentee(matrice_aug, n)
    print()

    # Appel récursif pour l'itération suivante
    return gauss_jordan_systeme_recursive(A, b, k + 1, matrice_aug)


def gauss_jordan_inverse_recursive(A, k=0, matrice_aug=None):
    """
    Calcule la matrice inverse A^(-1) par Gauss-Jordan (version récursive)

    Paramètres:
        A: matrice carrée
        k: indice de l'itération courante
        matrice_aug: matrice augmentée [A | I]

    Retourne:
        A_inv: matrice inverse
    """
    n = len(A)

    # Initialisation
    if matrice_aug is None:
        I = creer_matrice_identite(n)
        matrice_aug = former_matrice_augmentee(A, I)
        print("La matrice A :")
        afficher_matrice(A)
        print("\n// Former la matrice augmentée [A | I]")
        afficher_matrice_augmentee_inverse(matrice_aug, n)
        print("\n--------------- Calcul de l'inverse par Gauss-Jordan (RÉCURSIF) -----------------\n")

    # Cas de base: toutes les itérations sont terminées
    if k >= n:
        A_inv = extraire_inverse(matrice_aug, n)
        print("// La partie droite de la matrice contient A^(-1)")
        print("* La matrice inverse A^(-1) :")
        afficher_matrice(A_inv)
        return A_inv

    # Itération k
    print(f"*** Itération k = {k + 1}")

    # Normalisation du pivot
    pivot = normaliser_pivot(matrice_aug, k, 2 * n)
    print(f"** pivot = {pivot}")

    print(f"* Après normalisation:")
    afficher_matrice_augmentee_inverse(matrice_aug, n)

    # Mise à zéro des autres lignes
    eliminer_autres_lignes(matrice_aug, k, 2 * n)

    print(f"* Après élimination:")
    afficher_matrice_augmentee_inverse(matrice_aug, n)
    print()

    # Appel récursif pour l'itération suivante
    return gauss_jordan_inverse_recursive(A, k + 1, matrice_aug)


