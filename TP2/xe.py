import sys

sys.path.append('../TP1')
from tp import determinantIterative as det, lireMatrice as lireA, isTriangulaireSuprieure as triS, \
    isTriangulaireInfrieure as triI
import time


def changeCol(mat, col, new):
    for i in range(len(mat)):
        mat[i][col] = new[i]


def copyMat(mat):
    n = len(mat)
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = mat[i][j]

    return new


def descenteITR(mat, b):
    if triS(mat) == True:
        print('must be sup')
        return None

    n = len(mat)
    x = []
    x.append(b[0] / mat[0][0])

    for i in range(1, n):
        somme = 0
        for j in range(i - 1, -1, -1):
            somme += mat[i][j] * x[j]
        x.append((b[i] - somme) / mat[i][i])
    return x


def descenteREC(mat, b, i=0, j=None, x=None, somme=0):
    if triS(mat) == True:
        print('must be sup')
        return None

    if x is None:
        x = [0.0] * len(mat)
    if j is None:
        j = i - 1

    if i == len(mat):
        return x

    if j >= 0:
        return descenteREC(mat, b, i, j - 1, x, somme + mat[i][j] * x[j])
    else:
        x[i] = (b[i] - somme) / mat[i][i]
        return descenteREC(mat, b, i + 1, None, x, 0)


def remontéeITR(mat, b):
    if triI(mat) == True:
        print('must be inf')
        return None

    n = len(mat)
    x = [0 for _ in range(n)]
    x[n - 1] = b[n - 1] / mat[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        somme = 0
        for j in range(i + 1, n):
            somme += mat[i][j] * x[j]
        x[i] = (b[i] - somme) / mat[i][i]
    return x


def remontéeREC(mat, b, i=None, j=None, x=None, somme=0):
    if triI(mat) == True:
        print('must be inf')
        return None

    n = len(b)
    if x is None:
        x = [0.0] * n
    if i is None:
        i = n - 1
    if j is None:
        j = i + 1

    if i < 0:
        return x

    if j < n:
        return remontéeREC(mat, b, i, j + 1, x, somme + mat[i][j] * x[j])
    else:
        x[i] = (b[i] - somme) / mat[i][i]
        return remontéeREC(mat, b, i - 1, None, x, 0)


def Cramer(mat, b):
    if det(mat) == 0:
        return None

    n = len(mat)
    x = []

    for i in range(n):
        submat = []

        for j in range(n):
            submat.append(mat[j][:i] + [b[j]] + mat[j][i + 1:])

        x.append(det(submat) / det(mat))

    return x


def RECramer(mat, b, i=0, x=None, detA=None, j=0, submat=None):
    n = len(mat)

    if x is None:
        x = []
        detA = det(mat)
        if detA == 0:
            return None

    if i == n:
        return x

    if submat is None:
        submat = []

    if j < n:
        row = mat[j][:i] + [b[j]] + mat[j][i + 1:]
        submat.append(row)
        return RECramer(mat, b, i, x, detA, j + 1, submat)

    xi = det(submat) / detA
    x.append(xi)

    return RECramer(mat, b, i + 1, x, detA)


def test():
    A1 = [[3, 2, 5],
          [0, 1, -3],
          [0, 0, 1]]

    b1 = [4, -2, 1]

    A2 = [[4, 1, -1, -2],
          [0, 3, -2, 1],
          [0, 0, 1, -1],
          [0, 0, 0, 1]]

    b2 = [0, 5, 1, -1]

    A3 = [[-2, 0, 0],
          [-1, 3, 0],
          [4, 1, 3]]

    b3 = [4, -1, 0]

    A4 = [[2, 0, 0, 0],
          [-1, 2, 0, 0],
          [4, -1, 3, 0],
          [1, 3, -3, 2]]

    b4 = [-4, 6, -1, -15]

    pairs = [
        (A1, b1, [remontéeITR, remontéeREC, Cramer, RECramer]),
        (A2, b2, [remontéeITR, remontéeREC, Cramer, RECramer]),
        (A3, b3, [descenteITR, descenteREC, Cramer, RECramer]),
        (A4, b4, [descenteITR, descenteREC, Cramer, RECramer])
    ]

    func_names = {
        remontéeITR: "remontée iterative",
        remontéeREC: "remontée recursive",
        descenteITR: "descente iterative",
        descenteREC: "descente recursive",
        Cramer: "Cramer iterative",
        RECramer: "Cramer recursive"
    }

    for idx, (A, b, funcs) in enumerate(pairs, 1):
        print(f"\nA{idx}:")
        for func in funcs:
            start = time.perf_counter_ns()
            result = func(A, b)
            end = time.perf_counter_ns()
            exc_ns = end - start
            print(f"{func_names[func]} result: {result} (time: {exc_ns} ns)")


def afficher(A, b):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(A[i][j], end="\t")
        print(f'| {b[i]}')


def lireb(n):
    b = []
    for i in range(n):
        b.append(int(input(f"b[{i}] = ")))
    return b


def main():
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
            A = lireA(n)
            b = lireb(n)
        if choice == 2:
            print("(A, b):")
            afficher(A, b)
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


test()
main()