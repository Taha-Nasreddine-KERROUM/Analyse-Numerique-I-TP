from tp4p1 import *


def gauss_jordan_solution_REC(mat, b, k=0, augmented=None, first_call=True):
    n = len(mat)

    if augmented is None:
        augmented = formMatAug(mat, [b])

    if first_call:
        print("La matrice augmentee [A | b] :")
        print_augmented_matrix(augmented, n)
        print()

    if k >= n:
        print("// Afficher le vecteur solution X")
        x = []

        AfficherX(x, augmented, n)

        print("* La solution :")
        printX(x)

        return x

    print(f"** Iteration k = {k + 1}")

    pivot = augmented[k][k]
    print(f"** Pivot = {pivot}")

    normaliserPivot(augmented, pivot, k)

    print(f"* Apres normalisation (ligne {k + 1}):")
    print_augmented_matrix(augmented, n)
    print()

    elemenateGJedition(augmented, k, n)

    print(f"* Apres elimination (colonne {k + 1}):")
    print_augmented_matrix(augmented, n)
    print()

    return gauss_jordan_solution_REC(mat, b, k + 1, augmented, False)



def gauss_jordan_inverse_REC(mat, k=0, augmented=None, first_call=True):
    n = len(mat)

    if augmented is None:
        identity = matriceDidentit(n)

        augmented = formMatAug(mat, list(zip(*identity)))

    if first_call:
        print("La matrice augmentee [A | I] :")
        print_augmented_matrix(augmented, n)
        print()

    if k >= n:
        inverse_A = partieDroite(augmented, n)

        print("// La partie droite de la matrice contient A^-1")
        print("* La matrice inverse A^-1 :")
        print_system(inverse_A)

        return inverse_A

    print(f"** Iteration k = {k + 1}")

    pivot = augmented[k][k]
    print(f"** Pivot = {pivot}")

    normaliserPivot(augmented, pivot, k)

    print(f"* Apres normalisation (ligne {k + 1}):")
    print_augmented_matrix(augmented, n)
    print()

    elemenateGJedition(augmented, k, n)

    print(f"* Apres elimination (colonne {k + 1}):")
    print_augmented_matrix(augmented, n)
    print()

    return gauss_jordan_inverse_REC(mat, k + 1, augmented, False)


def gauss_jordan_solution(mat, b):
    n = len(mat)

    augmented = formMatAug(mat, [b])

    print("La matrice augmentee [A | b] :")
    print_augmented_matrix(augmented, n)
    print()

    for k in range(n):
        print(f"** Iteration k = {k + 1}")

        pivot = augmented[k][k]
        print(f"** Pivot = {pivot}")

        normaliserPivot(augmented, pivot, k)

        print(f"* Apres normalisation (ligne {k + 1}):")
        print_augmented_matrix(augmented, n)
        print()

        elemenateGJedition(augmented, k, n)

        print(f"* Apres elimination (colonne {k + 1}):")
        print_augmented_matrix(augmented, n)
        print()

    print("// Afficher le vecteur solution X")
    x = []
    AfficherX(x, augmented, n)

    print("* La solution :")
    printX(x)

    return x


def gauss_jordan_inverse(mat):
    n = len(mat)

    identity = matriceDidentit(n)

    augmented = formMatAug(mat, list(zip(*identity)))

    print("La matrice augmentee [A | I] :")
    print_augmented_matrix(augmented, n)
    print()

    for k in range(n):
        print(f"** Iteration k = {k + 1}")

        pivot = augmented[k][k]
        print(f"** Pivot = {pivot}")

        normaliserPivot(augmented, pivot, k)

        print(f"* Apres normalisation (ligne {k + 1}):")
        print_augmented_matrix(augmented, n)
        print()

        elemenateGJedition(augmented, k, n)

        print(f"* Apres elimination (colonne {k + 1}):")
        print_augmented_matrix(augmented, n)
        print()

    inverse_A = partieDroite(augmented, n)

    print("// La partie droite de la matrice contient A^-1")
    print("* La matrice inverse A^-1 :")
    print_system(inverse_A)

    return inverse_A