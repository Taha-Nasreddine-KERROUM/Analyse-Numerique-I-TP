from tp5 import *

def menuT1():
    A = None
    B = None
    n = 0

    while True:
        print("\nMenu:")
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

        choice = int(input("Choisissez 1,13: "))

        if choice == 1:
            n = int(input("Entrez N: "))
            print("Lecture de A:")
            A = lireMatrice(n)

        elif choice == 2:
            print("Matrice A:")
            print_system(A)
            if B is not None:
                print("Matrice B:")
                print_system(B)

        elif choice == 3:
            m = int(input("Entrez n: "))
            print("Matrice d'identité d'ordre", m, ":")
            print_system(matriceDidentit(m))

        elif choice == 4:
            if B is None:
                print("Lecture B:")
                B = lireMatrice(n)
            print("Somme est:")
            print_system(somme2matrices(A, B))

        elif choice == 5:
            if B is None:
                print("Lecture B:")
                B = lireMatrice(n)
            print("Produit est A et B:")
            print_system(produit2matrices(A, B))

        elif choice == 6:
            print("Transposée de A:")
            print_system(transpose(A))

        elif choice == 7:
            print("A est triangulaire supérieure." if isTriangulaireSuprieure(A) else "A n'est pas triangulaire supérieure.")

        elif choice == 8:
            print("A est triangulaire inférieure." if isTriangulaireInfrieure(A) else "A n'est pas triangulaire inférieure.")

        elif choice == 9:
            print("A est diagonale." if isDiagonale(A) else "A n'est pas diagonale.")

        elif choice == 10:
            print("A est symétrique." if isSymétrique(A) else "A n'est pas symétrique.")

        elif choice == 11:
            lin1 = int(input("Entrez la ligne 1: "))
            lin2 = int(input("Entrez la ligne 2: "))
            permet2liner(A, lin1, lin2)
            print_system(A)

        elif choice == 12:
            col1 = int(input("Entrez la colonne 1: "))
            col2 = int(input("Entrez la colonne 2: "))
            permet2col(A, col1, col2)
            print_system(A)

        elif choice == 13:
            print("""
            1- recursive
            2- iterative
            """)
            choice = int(input("Choisissez 1,2: "))
            if choice == 1:
                print("det|A|: ", determinant(A))
            elif choice == 2:
                print("det|A|: ", determinantIterative(A))

def menuT2():
    A = []
    b = []
    x = []

    while True:
        print("""
        1 - lire (A, b)
        2 - afficher (A, b)
        3 - algo de descente
        4 - algo de remontée
        5 -algo de Cramer
        """)
        choice = int(input("Choisissez 1,5: "))
        if choice == 1:
            n = int(input("Entrez N: "))
            print("Lecture de A:")
            A = lireMatrice(n)
            b = lireb(n)
        if choice == 2:
            print("(A, b):")
            print_system(A, b)
        if choice == 3:
            choice = int(input("""
            1 - descente iterative
            2 - descente recursive: """))
            if choice == 1:
                start = time.perf_counter_ns()
                x = descenteITR(A, b)
                end = time.perf_counter_ns()
                exc_ns = end - start
                print(f'x = {x} (time: {exc_ns} ns)')
            if choice == 2:
                start = time.perf_counter_ns()
                x = descenteREC(A, b)
                end = time.perf_counter_ns()
                exc_ns = end - start
                print(f'x = {x} (time: {exc_ns} ns)')
        if choice == 4:
            choice = int(input('''
            1 - remontée iterative
            2 - remontée recursive: '''))
            if choice == 1:
                start = time.perf_counter_ns()
                x = remontéeITR(A, b)
                end = time.perf_counter_ns()
                exc_ns = end - start
                print(f'x = {x} (time: {exc_ns} ns)')
            if choice == 2:
                start = time.perf_counter_ns()
                x = remontéeREC(A, b)
                end = time.perf_counter_ns()
                exc_ns = end - start
                print(f'x = {x} (time: {exc_ns} ns)')
        if choice == 5:
            choice = int(input('''
            1 - Cramer iterative
            2 - Cramer recursive: '''))
            if choice == 1:
                start = time.perf_counter_ns()
                x = Cramer(A, b)
                end = time.perf_counter_ns()
                exc_ns = end - start
                print(f'x = {x} (time: {exc_ns} ns)')
            if choice == 2:
                start = time.perf_counter_ns()
                x = RECramer(A, b)
                end = time.perf_counter_ns()
                exc_ns = end - start
                print(f'x = {x} (time: {exc_ns} ns)')

def menuT3():
    while True:
        n = int(input("Entrez la taille de la matrice : "))

        A = lireMatrice(n)
        b = lireb(n)

        method = int(input("Choisissez la méthode (1-Normal, 2-Pivot Partiel, 3-Pivot Total) : "))
        choice = int(input("Choisissez (1-Itérative, 2-Récursive) : "))

        start_time = time.time()

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
                x = remontéeITR(A, b)
                reorder_x_after_column_swaps(x, col_perm)

            if choice == 2:
                print('\n--- Méthode Pivot Total Récursive ---\n')
                A, b, col_perm = triangularisationPLREC(A, b)
                x = remontéeITR(A, b)
                reorder_x_after_column_swaps(x, col_perm)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"execution time : {execution_time:.3f} s")
        input("Press any key to continue.")
        continue

def menuT4p1():
    print("Entrez la taille de la matrice:")
    n = int(input("n = "))

    print("\nEntrez la matrice A:")
    A = lireMatrice(n)

    print("\nEntrez le vecteur b:")
    b = lireb(n)

    choice = int(input("""
    1 - décomposition iterative
    2 - décomposition recursive:"""))

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


def menuT4p2():
    print("ALGORITHME DE GAUSS-JORDAN")
    print()

    print("Choisissez une option:")
    print("1. Resoudre un systeme Ax=b (iteratif)")
    print("2. Calculer la matrice inverse A^-1 (iteratif)")
    print("3. Resoudre un systeme Ax=b (recursif)")
    print("4. Calculer la matrice inverse A^-1 (recursif)")
    print("5. Toutes les methodes")

    choix = int(input("\nVotre choix (1/2/3/4/5): "))

    print("\nEntrez la taille de la matrice:")
    n = int(input("n = "))

    print("\nEntrez la matrice A:")
    A = lireMatrice(n)

    if choix == 1 or choix == 3 or choix == 5:
        print("\nEntrez le vecteur b:")
        b = lireb(n)

    if choix == 1 or choix == 5:
        print("PARTIE 1: RESOLUTION DU SYSTEME Ax=b (ITERATIF)")
        print()

        x = gauss_jordan_solution(copier_matrice(A), b[:])

        print("Solution finale:")
        printX(x)

    if choix == 2 or choix == 5:
        print("PARTIE 2: CALCUL DE LA MATRICE INVERSE A^-1 (ITERATIF)")
        print()

        A_inv = gauss_jordan_inverse(copier_matrice(A))

        print("Matrice inverse finale:")
        print_system(A_inv)

    if choix == 3 or choix == 5:
        print("PARTIE 3: RESOLUTION DU SYSTEME Ax=b (RECURSIF)")
        print()

        x_rec = gauss_jordan_solution_REC(copier_matrice(A), b[:])

        print("Solution finale:")
        printX(x_rec)

    if choix == 4 or choix == 5:
        print("PARTIE 4: CALCUL DE LA MATRICE INVERSE A^-1 (RECURSIF)")
        print()

        A_inv_rec = gauss_jordan_inverse_REC(copier_matrice(A))

        print("Matrice inverse finale:")
        print_system(A_inv_rec)

def menuT5():
    print("METHODES ITERATIVES")
    print()

    print("Choisissez une methode:")
    print("1. Methode de Jacobi (iterative)")
    print("2. Methode de Gauss-Seidel (iterative)")
    print("3. Methode de Jacobi (recursive)")
    print("4. Methode de Gauss-Seidel (recursive)")
    print("5. Toutes les methodes")

    choix = int(input("\nVotre choix (1/2/3/4/5): "))

    print("\nEntrez la taille de la matrice:")
    n = int(input("n = "))

    print("\nEntrez la matrice A:")
    A = lireMatrice(n)

    print("\nEntrez le vecteur b:")
    b = lireb(n)

    print("\nEntrez le nombre maximum d'iterations:")
    n_max = int(input("N max = "))

    print("\nEntrez la precision (epsilon) [default: 1e-6]:")
    try:
        epsilon = float(input("epsilon = "))
    except:
        epsilon = 1e-6

    if choix == 1 or choix == 5:
        print("\n")
        print("METHODE DE JACOBI (ITERATIVE)")
        print()

        x_jacobi = jacobi(copier_matrice(A), b[:], n_max, epsilon)

    if choix == 2 or choix == 5:
        print("\n")
        print("METHODE DE GAUSS-SEIDEL (ITERATIVE)")
        print()

        x_gs = gauss_seidel(copier_matrice(A), b[:], n_max, epsilon)

    if choix == 3 or choix == 5:
        print("\n")
        print("METHODE DE JACOBI (RECURSIVE)")
        print()

        x_jacobi_rec = jacobi_REC(copier_matrice(A), b[:], n_max, epsilon)

    if choix == 4 or choix == 5:
        print("\n")
        print("METHODE DE GAUSS-SEIDEL (RECURSIVE)")
        print()

        x_gs_rec = gauss_seidel_REC(copier_matrice(A), b[:], n_max, epsilon)

def MainMenu():
    while True:
        start = time.perf_counter_ns()

        choice = int(input("""
        1- basic concepts
        2- Crammer
        3- Gauss
        4- Algorithme de décomposition LU
        5- ALGORITHME DE GAUSS-JORDAN
        6- METHODES ITERATIVES"""))

        if choice == 1:
            menuT1()
        elif choice == 2:
            menuT2()
        elif choice == 3:
            menuT3()
        elif choice == 4:
            menuT4p1()
        elif choice == 5:
            menuT4p2()
        elif choice == 6:
            menuT5()

        end = time.perf_counter_ns()
        exc_ns = end - start
        print(f"execution time : {exc_ns} ns")