import numpy as np

numbers = list(map(int, input("Nhập các hệ số c: ").split()))


def generate_matrix_2x2(c=0):

    matrix = np.zeros((2, 2), dtype=int)
    matrix[0][1] = 1
    matrix[1][0] = 1
    matrix[0][0] = c
    return matrix


def calculate_pn_qn(numbers):
    result = generate_matrix_2x2(numbers[0])

    for i in range(1, len(numbers)):
        result = np.dot(result, generate_matrix_2x2(numbers[i]))

    return result[0][0], result[1][0]


pn, qn = calculate_pn_qn(numbers)

print(f"pn: {pn}\nqn: {qn}")
