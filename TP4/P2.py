from helper import *


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