def print_system(mat, b):
    print("Le système est :")
    n = len(mat)
    for i in range(n):
        print(f"[ {' '.join([f'{mat[i][j]:.4f}' for j in range(n)])} ] [ {b[i]:.4f} ]")
    print()


def print_step_tri(mat, b, k):
    print(f"* Itération K= {k} :")
    print_system(mat, b)


def print_step_rem(x):
    print("* La resolution donne :")
    for i in range(len(x)):
        print(f"X_{i + 1} = {x[i]:.6f} ;")
    print()


def print_gauss_header(mat, b):
    print("-------------- Gauss ---------------")
    print("* La matrice reduite :")
    print_system(mat, b)


def triangularisation(mat, b):
    n = len(mat)
    print_system(mat, b)

    if null_in_diagonal(mat):
        print('null detected')
        return None, None

    for k in range(n - 1):
        pivote = mat[k][k]

        eliminate(mat, b, k, pivote)

        print_step_tri(mat, b, k)
        if isTriangulaireSuprieure(mat):
            break

    print_gauss_header(mat, b)
    return mat, b


def triangularisationREC(mat, b, k=0):
    n = len(mat)

    if k == 0:
        print_system(mat, b)
        if null_in_diagonal(mat):
            print('null detected')
            return None, None

    if k >= n - 1 or isTriangulaireSuprieure(mat):
        print_gauss_header(mat, b)
        return mat, b

    pivote = mat[k][k]
    if pivote != 0:
        eliminate(mat, b, k, pivote)

    print_step_tri(mat, b, k)
    return triangularisationREC(mat, b, k + 1)


def remontee(mat, b):
    n = len(mat)
    x = [0] * n
    if mat[n - 1][n - 1] == 0:
        print("mat[", n - 1, "][", n - 1, "] = 0")
        return None

    x[n - 1] = b[n - 1] / mat[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        somme = 0
        for k in range(i + 1, n):
            somme += mat[i][k] * x[k]

        if mat[i][i] == 0:
            print("mat[", i, "][", i, "] = 0")
            return None

        x[i] = (b[i] - somme) / mat[i][i]

    print_step_rem(x)
    return x


def eliminate(mat, b, k, pivot):
    if pivot == 0:
        print(f"pivot {pivot} = 0")
        raise Exception("pivot nul")
    n = len(mat)
    for i in range(k + 1, n):
        c = mat[i][k] / pivot
        b[i] -= c * b[k]
        mat[i][k] = 0
        for j in range(k + 1, n):
            mat[i][j] -= c * mat[k][j]


def remHelper(mat, x, i, n):
    somme = 0
    for k in range(i + 1, n):
        somme += mat[i][k] * x[k]
    return somme


def remonteeREC(mat, b, i=None, x=None):
    n = len(mat)
    if x is None:
        x = [0] * n
        i = n - 1

    if i < 0:
        print_step_rem(x)
        return x

    somme = remHelper(mat, x, i, n)

    if mat[i][i] == 0:
        print("mat[", i, "][", i, "] = 0")
        return None
    x[i] = (b[i] - somme) / mat[i][i]

    return remonteeREC(mat, b, i - 1, x)


def lireMat(n):
    return [[float(input(f"A[{i}][{j}] = ")) for j in range(n)] for i in range(n)]


def lireb(n):
    return [float(input(f"b[{i}] = ")) for i in range(n)]


def isTriangulaireSuprieure(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True


def null_in_diagonal(mat):
    n = len(mat)
    for i in range(n):
        if mat[i][i] == 0:
            return True
    return False