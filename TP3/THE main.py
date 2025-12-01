from P3 import *

import time

def main():
    while True:
        n = int(input("Entrez la taille de la matrice : "))

        A = lireMat(n)
        b = lireb(n)

        method = int(input("Choisissez la méthode (1-Normal, 2-Pivot Partiel, 3-Pivot Total) : "))
        choice = int(input("Choisissez (1-Itérative, 2-Récursive) : "))

        start_time = time.time()

        if method == 1:
            if choice == 1:
                print("\n--- Méthode Normale Itérative ---\n")
                A, b = triangularisation(A, b)
                remontee(A, b)
            else:
                print("\n--- Méthode Normale Récursive ---\n")
                A, b = triangularisationREC(A, b)
                remonteeREC(A, b)

        elif method == 2:
            if choice == 1:
                print("\n--- Méthode Pivot Partiel Itérative ---\n")
                A, b = triangularisationPP(A, b)
                remontee(A, b)
            else:
                print("\n--- Méthode Pivot Partiel Récursive ---\n")
                A, b = triangularisationPPREC(A, b)
                remonteeREC(A, b)

        elif method == 3:
            if choice == 1:
                print('\n--- Méthode Pivot Total Itérative ---\n')
                A, b, col_perm = triangularisationPL(A, b)
                x = remontee(A, b)
                reorder_x_after_column_swaps(x, col_perm)

            if choice == 2:
                print('\n--- Méthode Pivot Total Récursive ---\n')
                A, b, col_perm = triangularisationPLREC(A, b)
                x = remontee(A, b)
                reorder_x_after_column_swaps(x, col_perm)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"execution time : {execution_time:.3f} s")
        input("Press any key to continue.")
        continue

main()