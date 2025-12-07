from copy import deepcopy

from tp5 import *

def CramerMenu(M = None, l = None):
    while True:
        A, b = deepcopy(M), deepcopy(l)

        try:
            choice = int(input('''
            1 - Cramer iterative
            2 - Cramer recursive
            : '''))
        except:
            break

        if choice == 1:
            x = Cramer(A, b)
        elif choice == 2:
            x = RECramer(A, b)
        else:
            print("Choix incorrect")
            continue

        print("Solution finale:")
        printX(x)


def SeidelMenu(M = None, l = None):
    while True:
        A, b = deepcopy(M), deepcopy(l)

        try:
            method = int(input("Choisissez la méthode (1-Pivot non nul, 2-Pivot Partiel, 3-Pivot Total) : "))
            choice = int(input("Choisissez (1-Itérative, 2-Récursive) : "))
        except:
            break

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


def decoLUmenu(M = None, l = None):
    while True:
        A, b = deepcopy(M), deepcopy(l)

        try:
            choice = int(input("""
                1 - décomposition iterative
                2 - décomposition recursive
                : """))
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


def JordanMenu(M = None, l = None):
    while True:
        A, b = deepcopy(M), deepcopy(l)

        print("ALGORITHME DE GAUSS-JORDAN")
        print()

        print("Choisissez une option:")
        print("1. Resoudre un systeme Ax=b")
        print("2. Calculer la matrice inverse A^-1")
        print("3. Toutes les methodes")

        try:
            choix = int(input("\nVotre choix (1/2/3): "))
        except:
            break

        if choix == 1 or choix == 3:
            if choix != 3:
                print("""
                1. iterative
                2. recursive
                : """)
                try:
                    choix = int(input("Votre choix (1/2): "))
                except:
                    continue

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
                try:
                    choix = int(input("Votre choix (1/2): "))
                except:
                    continue

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


def methIter(M = None, l = None):
    M, l = setAb(M, l)

    while True:
        A, b = deepcopy(M), deepcopy(l)

        print("METHODES ITERATIVES")
        print()

        print("Choisissez une methode:")
        print("1. Methode de Jacobi")
        print("2. Methode de Gauss-Seidel")
        print("3. Toutes les methodes")

        try:
            choix = int(input("\nVotre choix (1/2/3): "))
        except:
            break

        print("\nEntrez le nombre maximum d'iterations [default: 10]:")
        try:
            n_max = int(input("N max = "))
        except:
            n_max = 10

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
                try:
                    choix = int(input("Votre choix (1/2): "))
                except:
                    continue

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
                try:
                    choix = int(input("Votre choix (1/2): "))
                except:
                    continue

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


def methDirect(M = None, l = None):
    M, l = setAb(M, l)

    while True:
        A, b = deepcopy(M), deepcopy(l)
        print('''
        1. Cramer
        2. Gauss-Seidel
        3. decomposition LU
        4. Gauss-Jordan''')
        try:
            choix = int(input("Votre choix (1/2/3) or anything for out: "))
        except:
            break

        if choix == 1:
            CramerMenu(A, b)
        elif choix == 2:
            SeidelMenu(A, b)
        elif choix == 3:
            decoLUmenu(A, b)
        elif choix == 4:
            JordanMenu(A, b)

    return M, l


def MainMenu():
    A = None
    b = None

    while True:
        start = time.perf_counter_ns()

        try:
            choice = int(input("""
                1- lire (A, b)
                2- afficher (A, b)
                3- METHODES DIRECT
                4- METHODES ITERATIVES
                : """))
        except:
            continue

        if choice == 0:
            break

        elif choice == 1:
            try:
                n = int(input("Entrez N: "))
                print("Lecture de A:")
                A = lireMatrice(n)
                b = lireb(n)
            except:
                pass

        elif choice == 2:
            if A is None or b is None:
                print('must read first')
                continue

            print("(A, b):")
            print_system(A, b)

        elif choice == 3:
            A, b = methDirect(A, b)

        elif choice == 4:
            A, b = methIter(A, b)

        end = time.perf_counter_ns()
        exc_ns = end - start
        exc_s = exc_ns / 1e9
        print(f"execution time : {exc_s} s")

MainMenu()