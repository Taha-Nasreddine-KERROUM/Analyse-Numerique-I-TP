from helpers import *


def jacobi(mat, b, n_max, epsilon=1e-6):
    n = len(mat)

    x_old = [0.0] * n
    x_new = [0.0] * n

    print(f"Initialisation: x^(0) = {x_old}")
    print()

    for k in range(n_max):
        print(f"---------- Iteration k = {k + 1} ----------")

        for i in range(n):
            somme = 0

            for j in range(n):
                if j != i:
                    somme = somme + mat[i][j] * x_old[j]

            x_new[i] = (b[i] - somme) / mat[i][i]

            print(f"x_{i + 1}^({k + 1}) = (b[{i}] - somme) / A[{i}][{i}]")
            print(f"x_{i + 1}^({k + 1}) = ({b[i]:.4f} - {somme:.4f}) / {mat[i][i]:.4f}")
            print(f"x_{i + 1}^({k + 1}) = {x_new[i]:.6f}")
            print()

        print(f"Resultat iteration {k + 1}:")
        for i in range(n):
            print(f"x_{i + 1}^({k + 1}) = {x_new[i]:.6f}")
        print()

        converged = True
        for i in range(n):
            if abs(x_new[i] - x_old[i]) > epsilon:
                converged = False
                break

        if converged:
            print(f"Convergence atteinte a l'iteration {k + 1}")
            break

        x_old = x_new[:]

    print("\n")
    print("Solution finale:")
    printX(x_new)

    return x_new

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


def gauss_seidel(mat, b, n_max, epsilon=1e-6):
    n = len(mat)

    x = [0.0] * n
    x_old = [0.0] * n

    print(f"Initialisation: x^(0) = {x}")
    print()

    for k in range(n_max):
        print(f"---------- Iteration k = {k} ----------")

        x_old = x[:]

        for i in range(n):
            somme_1 = sumGauss(mat, i, i, 0, x)
            somme_2 = sumGauss(mat, n, i, i + 1, x)

            x[i] = (b[i] - somme_1 - somme_2) / mat[i][i]

            print(f"x_{i + 1}^({k + 1}) = (b[{i}] - somme_1 - somme_2) / A[{i}][{i}]")
            print(f"x_{i + 1}^({k + 1}) = ({b[i]:.4f} - {somme_1:.4f} - {somme_2:.4f}) / {mat[i][i]:.4f}")
            print(f"x_{i + 1}^({k + 1}) = {x[i]:.6f}")
            print()

        print(f"Resultat iteration {k + 1}:")
        for i in range(n):
            print(f"x_{i + 1}^({k + 1}) = {x[i]:.6f}")
        print()

        converged = True
        for i in range(n):
            if abs(x[i] - x_old[i]) > epsilon:
                converged = False
                break

        if converged:
            print(f"Convergence atteinte a l'iteration {k + 1}")
            break

    print("\n")
    print("Solution finale:")
    printX(x)

    return x


def jacobi_REC(mat, b, n_max, epsilon=1e-6, k=0, x_old=None, x_new=None):
    n = len(mat)

    if x_old is None:
        x_old = [0.0] * n
        x_new = [0.0] * n
        print(f"Initialisation: x^(0) = {x_old}")
        print()

    if k >= n_max:
        print("\n")
        print("Solution finale:")
        printX(x_new)
        return x_new

    if k > 0:
        converged = True
        for i in range(n):
            if abs(x_new[i] - x_old[i]) > epsilon:
                converged = False
                break

        if converged:
            print(f"Convergence atteinte a l'iteration {k}")
            print("\n")
            print("Solution finale:")
            printX(x_new)
            return x_new

    print(f"---------- Iteration k = {k + 1} ----------")

    x_temp = [0.0] * n
    for i in range(n):
        somme = 0
        for j in range(n):
            if j != i:
                somme = somme + mat[i][j] * x_old[j]

        x_temp[i] = (b[i] - somme) / mat[i][i]

        print(f"x_{i + 1}^({k + 1}) = (b[{i}] - somme) / A[{i}][{i}]")
        print(f"x_{i + 1}^({k + 1}) = ({b[i]:.4f} - {somme:.4f}) / {mat[i][i]:.4f}")
        print(f"x_{i + 1}^({k + 1}) = {x_temp[i]:.6f}")
        print()

    print(f"Resultat iteration {k + 1}:")
    for i in range(n):
        print(f"x_{i + 1}^({k + 1}) = {x_temp[i]:.6f}")
    print()

    return jacobi_REC(mat, b, n_max, epsilon, k + 1, x_temp, x_temp)


def gauss_seidel_REC(mat, b, n_max, epsilon=1e-6, k=0, x=None, x_old=None):
    n = len(mat)

    if x is None:
        x = [0.0] * n
        x_old = [0.0] * n
        print(f"Initialisation: x^(0) = {x}")
        print()

    if k >= n_max:
        print("\n" + "=" * 50)
        print("Solution finale:")
        printX(x)
        return x

    if k > 0:
        converged = True
        for i in range(n):
            if abs(x[i] - x_old[i]) > epsilon:
                converged = False
                break

        if converged:
            print(f"Convergence atteinte a l'iteration {k}")
            print("\n" + "=" * 50)
            print("Solution finale:")
            printX(x)
            return x

    print(f"---------- Iteration k = {k} ----------")

    x_old = x[:]

    for i in range(n):
        somme_1 = 0
        somme_2 = 0

        for j in range(i):
            somme_1 = somme_1 + mat[i][j] * x[j]

        for j in range(i + 1, n):
            somme_2 = somme_2 + mat[i][j] * x[j]

        x[i] = (b[i] - somme_1 - somme_2) / mat[i][i]

        print(f"x_{i + 1}^({k + 1}) = (b[{i}] - somme_1 - somme_2) / A[{i}][{i}]")
        print(f"x_{i + 1}^({k + 1}) = ({b[i]:.4f} - {somme_1:.4f} - {somme_2:.4f}) / {mat[i][i]:.4f}")
        print(f"x_{i + 1}^({k + 1}) = {x[i]:.6f}")
        print()

    print(f"Resultat iteration {k + 1}:")
    for i in range(n):
        print(f"x_{i + 1}^({k + 1}) = {x[i]:.6f}")
    print()

    return gauss_seidel_REC(mat, b, n_max, epsilon, k + 1, x, x_old)


if __name__ == "__main__":
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