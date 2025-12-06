from copy import deepcopy

from tp5 import *

def menuT1(M1 = None, M2 = None):
    while True:
        A, B = deepcopy(M1), deepcopy(M2)
        print("""
        1- Lire une matrice carrée de taille N.
        2- Afficher une matrice carrée de taille N.
        3- Afficher la matrice d’identité d’ordre N.
        4- Calculer la somme de deux matrices de même taille.
        5- Calculer le produit de deux matrices.
        6- Calculer la transposée d’une matrice carrée.
        7- Tester si une matrice est triangulaire supérieure.
        8- Tester si une matrice est triangulaire inférieure.
        9- Tester si une matrice carrée est diagonale.
        10- Tester si une matrice carrée est symétrique.
        11- permeter deux lignes de une matrice.
        12- permeter deux colonnes de une matrice.
        13- determinant.
        """)

        choice = input("Choisissez 1,13 or anything for out: ")

        try:
            choice = int(choice)
        except:
            break

        if choice == 1:
            n = int(input("Entrez N: "))
            print("Lecture de A:")
            M1 = lireMatrice(n)
            print("Lecture de B:")
            M2 = lireMatrice(n)

        elif choice == 2:
            affprintTp1(A)
            affprintTp1(B, 'B')

        elif choice == 3:
            m = int(input("Entrez n: "))
            print("Matrice d'identité d'ordre", m, ":")
            print_system(matriceDidentit(m))

        elif choice == 4:
            sommeTp1(A, B)

        elif choice == 5:
            prodTp1(A, B)

        elif choice == 6:
            transTp1(A)
            transTp1(B, 'B')

        elif choice == 7:
            tringlsupTp1(A)
            tringlsupTp1(B, 'B')

        elif choice == 8:
            tringlinfTp1(A)
            tringlinfTp1(B, 'B')

        elif choice == 9:
            diagnlTp1(A)
            diagnlTp1(B, 'B')

        elif choice == 10:
            symtrqTp1(A)
            symtrqTp1(B, 'B')

        elif choice == 11:
            per2linertp1(A)
            per2linertp1(B, 'B')

        elif choice == 12:
            per2coltp1(A)
            per2coltp1(B, 'B')

        elif choice == 13:
            determinant(A)
            detp1Choice(B, 'B')

        else:
            break

    return M1, M2

def menuT2(M = None, l = None):
    x = []

    while True:
        A, b = deepcopy(M), deepcopy(l)

        print("""
        1 - lire (A, b)
        2 - afficher (A, b)
        3 - algo de descente
        4 - algo de remontée
        5 - algo de Cramer
        """)
        choice = input("Choisissez 1,5 or anything for out: ")

        try:
            choice = int(choice)
        except:
            break

        if choice == 1:
            n = int(input("Entrez N: "))
            print("Lecture de A:")
            M = lireMatrice(n)
            l = lireb(n)

        elif choice == 2:
            if A is None or b is None:
                print('must read first')
                continue

            print("(A, b):")
            print_system(A, b)

        elif choice == 3:
            if A is None or b is None:
                print('must read first')
                continue

            choice = int(input("""
            1 - descente iterative
            2 - descente recursive
            : """))

            if choice == 1:
                x = descenteITR(A, b)
            elif choice == 2:
                x = descenteREC(A, b)
            else:
                print("Choix incorrect")
                continue

            print("Solution finale:")
            printX(x)

        elif choice == 4:
            if A is None or b is None:
                print('must read first')
                continue

            choice = int(input('''
            1 - remontée iterative
            2 - remontée recursive
            : '''))

            if choice == 1:
                x = remontéeITR(A, b)
            elif choice == 2:
                x = remontéeREC(A, b)
            else:
                print("Choix incorrect")
                continue

            print("Solution finale:")
            printX(x)

        elif choice == 5:
            if A is None or b is None:
                print('must read first')
                continue

            choice = int(input('''
            1 - Cramer iterative
            2 - Cramer recursive
            : '''))

            if choice == 1:
                x = Cramer(A, b)
            elif choice == 2:
                x = RECramer(A, b)
            else:
                print("Choix incorrect")
                continue

            print("Solution finale:")
            printX(x)

        else:
            break

    return M, l

def menuT3(M = None, l = None):
    M, l = setAb(M, l)

    while True:
        A, b = deepcopy(M), deepcopy(l)
        method = input("Choisissez la méthode (1-Pivot non nul, 2-Pivot Partiel, 3-Pivot Total) : ")

        try:
            method = int(method)
        except:
            break

        choice = int(input("Choisissez (1-Itérative, 2-Récursive) : "))

        if method == 1:
            if choice == 1:
                print("\n--- Méthode Normale Itérative ---\n")
                A, b = triangularisation(A, b)
                remontéeITR(A, b)
            else:
                print("\n--- Méthode Normale Récursive ---\n")
                A, b = triangularisationREC(A, b)
                remontéeITR(A, b)

        elif method == 2:
            if choice == 1:
                print("\n--- Méthode Pivot Partiel Itérative ---\n")
                A, b = triangularisationPP(A, b)
                remontéeITR(A, b)
            else:
                print("\n--- Méthode Pivot Partiel Récursive ---\n")
                A, b = triangularisationPPREC(A, b)
                remontéeITR(A, b)

        elif method == 3:
            if choice == 1:
                print('\n--- Méthode Pivot Total Itérative ---\n')
                A, b, col_perm = triangularisationPL(A, b)
                order(A, b, col_perm)

            if choice == 2:
                print('\n--- Méthode Pivot Total Récursive ---\n')
                A, b, col_perm = triangularisationPLREC(A, b)
                order(A, b, col_perm)

        else:
            break

    return M, l

def menuT4p1(M = None, l = None):
    M, l = setAb(M, l)

    while True:
        A, b = deepcopy(M), deepcopy(l)

        choice = input("""
        1 - décomposition iterative
        2 - décomposition recursive
        : """)

        try:
            choice = int(choice)
        except:
            break

        if choice == 1:
            print("\n")
            print("MÉTHODE ITÉRATIVE")

            x_iter = solve_LU(copier_matrice(A), b[:])

            print("\n")
            print("Solution finale (itérative):")
            printX(x_iter)

        elif choice == 2:
            print("\n")
            print("MÉTHODE RÉCURSIVE")

            x_rec = solve_LU_REC(copier_matrice(A), b[:])

            print("\n")
            print("Solution finale (récursive):")
            printX(x_rec)

        else:
            break

    return M, l

def menuT4p2(M = None, l = None):
    M, l = setAb(M, l)

    while True:
        A, b = deepcopy(M), deepcopy(l)

        print("ALGORITHME DE GAUSS-JORDAN")
        print()

        print("Choisissez une option:")
        print("1. Resoudre un systeme Ax=b")
        print("2. Calculer la matrice inverse A^-1")
        print("3. Toutes les methodes")

        choix = input("\nVotre choix (1/2/3): ")

        try:
            choix = int(choix)
        except:
            break

        if choix == 1 or choix == 3:
            if choix != 3:
                print("""
                1. iterative
                2. recursive
                : """)
                choix = int(input("Votre choix (1/2): "))

            if choix == 1 or choix == 3:
                print("PARTIE 1: RESOLUTION DU SYSTEME Ax=b (ITERATIF)")
                print()

                x = gauss_jordan_solution(copier_matrice(A), b[:])

                print("Solution finale:")
                printX(x)

            if choix == 2 or choix == 3:
                print("PARTIE 3: RESOLUTION DU SYSTEME Ax=b (RECURSIF)")
                print()

                x_rec = gauss_jordan_solution_REC(copier_matrice(A), b[:])

                print("Solution finale:")
                printX(x_rec)

        if choix == 2 or choix == 3:
            if choix != 3:
                print("""
                1. iterative
                2. recursive
                : """)
                choix = int(input("Votre choix (1/2): "))

            if choix == 1 or choix == 3:
                print("PARTIE 2: CALCUL DE LA MATRICE INVERSE A^-1 (ITERATIF)")
                print()

                A_inv = gauss_jordan_inverse(copier_matrice(A))

                print("Matrice inverse finale:")
                print_system(A_inv)

            if choix == 2 or choix == 3:
                print("PARTIE 4: CALCUL DE LA MATRICE INVERSE A^-1 (RECURSIF)")
                print()

                A_inv_rec = gauss_jordan_inverse_REC(copier_matrice(A))

                print("Matrice inverse finale:")
                print_system(A_inv_rec)

        if not valid(choix, 1, 3):
            break

    return M, l

def menuT5(M = None, l = None):
    M, l = setAb(M, l)

    while True:
        A, b = deepcopy(M), deepcopy(l)

        print("METHODES ITERATIVES")
        print()

        print("Choisissez une methode:")
        print("1. Methode de Jacobi")
        print("2. Methode de Gauss-Seidel")
        print("3. Toutes les methodes")

        choix = input("\nVotre choix (1/2/3): ")

        try:
            choix = int(choix)
        except:
            break

        print("\nEntrez le nombre maximum d'iterations:")
        n_max = int(input("N max = "))

        print("\nEntrez la precision (epsilon) [default: 1e-10]:")
        try:
            epsilon = float(input("epsilon = "))
        except:
            epsilon = 1e-10

        if choix == 1 or choix == 3:
            if choix != 5:
                print("""
                1. iterative
                2. recursive
                : """)
                choix = int(input("Votre choix (1/2): "))

            if choix == 1 or choix == 5:
                print("\n")
                print("METHODE DE JACOBI (ITERATIVE)")
                print()

                x_jacobi = jacobi(copier_matrice(A), b[:], n_max, epsilon)

            if choix == 2 or choix == 5:
                print("\n")
                print("METHODE DE JACOBI (RECURSIVE)")
                print()

                x_jacobi_rec = jacobi_REC(copier_matrice(A), b[:], n_max, epsilon)

        if choix == 2 or choix == 3:
            if choix != 3:
                print("""
                1. iterative
                2. recursive
                : """)
                choix = int(input("Votre choix (1/2): "))

            if choix == 1 or choix == 3:
                print("\n")
                print("METHODE DE GAUSS-SEIDEL (ITERATIVE)")
                print()

                x_gs = gauss_seidel(copier_matrice(A), b[:], n_max, epsilon)

            if choix == 2 or choix == 3:
                print("\n")
                print("METHODE DE GAUSS-SEIDEL (RECURSIVE)")
                print()

                x_gs_rec = gauss_seidel_REC(copier_matrice(A), b[:], n_max, epsilon)

        if not valid(choix, 1, 3):
            break

    return M, l

def MainMenu():
    A = None
    b = None
    B = None

    while True:
        start = time.perf_counter_ns()

        choice = input("""
        1- basic concepts
        2- Crammer
        3- Gauss
        4- Algorithme de décomposition LU
        5- ALGORITHME DE GAUSS-JORDAN
        6- METHODES ITERATIVES
        : """)

        try:
            choice = int(choice)
        except:
            continue

        if choice == 0:
            break
        elif choice == 1:
            A, B = menuT1(A, B)
        elif choice == 2:
            A, b = menuT2(A, b)
        elif choice == 3:
            A, b = menuT3(A, b)
        elif choice == 4:
            A, b = menuT4p1(A, b)
        elif choice == 5:
            A, b = menuT4p2(A, b)
        elif choice == 6:
            A, b = menuT5(A, b)

        end = time.perf_counter_ns()
        exc_ns = end - start
        exc_s = exc_ns / 1e9
        print(f"execution time : {exc_s} s")

MainMenu()