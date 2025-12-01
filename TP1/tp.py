def lireMatrice(n):
    mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(input(f"mat[{i}][{j}] = "))
    return mat


def afficherMatrice(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end="\t")
        print()


def matriceDidentit(n):
    mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        mat[i][i] = 1
    return mat


def somme2matrices(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def produit2matrices(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def transpose(A):
    n = len(A)
    AT = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            AT[j][i] = A[i][j]
    return AT


def isTriangulaireSuprieure(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True


def isTriangulaireInfrieure(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j] != 0:
                return False
    return True


def isDiagonale(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if i != j and mat[i][j] != 0:
                return False
    return True


def isSymétrique(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j] != mat[j][i]:
                return False
    return True


def determinant(A, row=0, mask=0, col=0, prod=1, parity=0):
    """
    - A: square matrix (list of lists)
    - row: current row we are assigning
    - mask: bitmask of chosen columns (bit i set => column i already used)
    - col: current column being considered for the current row (used to simulate a loop)
    - prod: product of A[i][perm[i]] accumulated so far
    - parity: total inversion count so far (parity determines sign)
    """
    n = len(A)
    # when a column for every row is chosen return signed product
    if row == n:
        return (-1) ** parity * prod

    # when tried all columns for this row
    if col == n:
        return 0

    # check if this column is already used
    if (mask >> col) & 1:
        return determinant(A, row, mask, col + 1, prod, parity)

    # number of previously chosen columns with index > col contributes to inversions:
    higher_mask = mask >> (col + 1)
    inv = higher_mask.bit_count() if hasattr(int, "bit_count") else bin(higher_mask).count("1") # if your python < 3.8

    # choose this column for current row, descend to next row so reset col to 0
    choose = determinant(A, row + 1, mask | (1 << col), 0, prod * A[row][col], parity + inv)

    # skip this column and try next column for the same row
    skip = determinant(A, row, mask, col + 1, prod, parity)

    return choose + skip


def determinantIterative(mat):
    if isTriangulaireSuprieure(mat) or isTriangulaireInfrieure(mat):
        det = mat[0][0]
        for i in range(1, len(mat)):
            det *= mat[i][i]
        return det

    stack = [(mat, 1)]
    det = 0
    while stack:
        mat, mult = stack.pop()
        n = len(mat)

        if n == 1:
            det += mult * mat[0][0]
            continue

        if n == 2:
            det += mult * mat[0][0] * mat[1][1] - mult * mat[0][1] * mat[1][0]
            continue

        for col in range(n):
            sign = (-1) ** col
            lilmat = []
            for i in range(1, n):
                row = []
                for j in range(n):
                    if j != col:
                        row.append(mat[i][j])
                lilmat.append(row)
            stack.append((lilmat, mult * sign * mat[0][col]))

    return det


def permet2liner(mat, lin1, lin2):
    n = len(mat)
    for i in range(n):
        mat[lin1][i], mat[lin2][i] = mat[lin2][i], mat[lin1][i]


def permet2col(mat, col1, col2):
    n = len(mat)
    for i in range(n):
        mat[i][col1], mat[i][col2] = mat[i][col2], mat[i][col1]


def menu():
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
            afficherMatrice(A)
            if B is not None:
                print("Matrice B:")
                afficherMatrice(B)

        elif choice == 3:
            m = int(input("Entrez n: "))
            print("Matrice d'identité d'ordre", m, ":")
            afficherMatrice(matriceDidentit(m))

        elif choice == 4:
            if B is None:
                print("Lecture B:")
                B = lireMatrice(n)
            print("Somme est:")
            afficherMatrice(somme2matrices(A, B))

        elif choice == 5:
            if B is None:
                print("Lecture B:")
                B = lireMatrice(n)
            print("Produit est A et B:")
            afficherMatrice(produit2matrices(A, B))

        elif choice == 6:
            print("Transposée de A:")
            afficherMatrice(transpose(A))

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
            afficherMatrice(A)

        elif choice == 12:
            col1 = int(input("Entrez la colonne 1: "))
            col2 = int(input("Entrez la colonne 2: "))
            permet2col(A, col1, col2)
            afficherMatrice(A)

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

#menu()