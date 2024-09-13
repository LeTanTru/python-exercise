import numpy as np


def minor_matrix(matrix, i, j):
    """
    Tạo ma trận con (n-1)x(n-1) bằng cách loại bỏ dòng i và cột j của ma trận matrix.
    """
    return np.delete(np.delete(matrix, i, axis=0), j, axis=1)


def cofactor_matrix(matrix):
    """
    Tính ma trận hệ số kép của ma trận matrix.
    """
    n = len(matrix)
    cofactor_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            minor = minor_matrix(matrix, i, j)
            cofactor_matrix[i][j] = ((-1) ** (i + j)) * np.linalg.det(minor)

    return cofactor_matrix.T


def adjoint_matrix(matrix):
    return cofactor_matrix(matrix).T


A = np.array([[1, 2, 3], [-1, 0, 4], [2, 5, -1]])
# B = np.array([[2, 0, 1], [3, 0, 0], [5, 1, 1]])

C = cofactor_matrix(A)
D = C.T
print("Ma trận hệ số kép của ma trận A:")
print(C)
print("Ma trận liên hợp của ma trận A:")
print(D)
