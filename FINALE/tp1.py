def lireMatrice(n):
    return [[float(input(f"A[{i}][{j}] = ")) for j in range(n)] for i in range(n)]


def print_system(mat, b=None):
    print("Le système est :")
    n = len(mat)
    for i in range(n):
        row = f"[ {' '.join([f'{mat[i][j]:.4f}' for j in range(n)])} ]"

        if b is not None:
            row += f" [ {b[i]:.4f} ]"

        print(row)
    print()


def matriceDidentit(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


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
    mat[lin1], mat[lin2] = mat[lin2], mat[lin1]


def permet2col(mat, col1, col2):
    n = len(mat)
    for i in range(n):
        mat[i][col1], mat[i][col2] = mat[i][col2], mat[i][col1]