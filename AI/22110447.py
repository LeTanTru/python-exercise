import numpy as np


def transpose(mat):
    return np.transpose(mat)


def product(mat_a, mat_b):
    try:
        result = np.dot(mat_a, mat_b)
        return result
    except ValueError:
        return "Khong co tich ma tran"


def hadamard_product(mat_a, mat_b):
    try:
        result = np.multiply(mat_a, mat_b)
        return result
    except ValueError:
        return "Khong co tich Hadamard"


def replace_col(mat, col_ind):
    mat[:, col_ind] = 1
    return mat


def is_out_of_column_range(mat, col_ind):
    num_cols = mat.shape[1]

    return not 0 <= col_ind < num_cols


def input_matrix(matrix_name):
    # Nhập số hàng và số cột cho ma trận A
    row = int(input(f"Nhập số hàng của ma trận {matrix_name}: "))
    col = int(input(f"Nhập số cột của ma trận {matrix_name}: "))

    # Nhập các phần tử của ma trận A từ người dùng
    print(
        f"Nhập các phần tử của ma trận {matrix_name} (mỗi phần tử cách nhau bằng khoảng trắng):"
    )
    elements = []
    for i in range(row):
        row_input = input(f"Nhập hàng {i+1} của ma trận {matrix_name}: ")
        row_values = list(map(float, row_input.split()))
        if len(row_values) != col:
            raise ValueError(
                f"Số lượng phần tử không khớp với số cột của ma trận {matrix_name}"
            )
        elements.append(row_values)

    # Tạo ma trận A từ danh sách nhập từ người dùng
    mat = np.array(elements)
    return mat


def main():
    while True:
        try:
            matrix_A = input_matrix("A")
            matrix_B = input_matrix("B")

            # # Hiển thị ma trận A và B
            print("\nMa trận A:")
            print(matrix_A)

            print("\nMa trận B:")
            print(matrix_B)

            matrix_transpose = transpose(matrix_A)
            print(f"Ma trận chuyển vị của ma trận A:\n{matrix_transpose}")
            matrix_transpose = transpose(matrix_B)
            print(f"Ma trận chuyển vị của ma trận B:\n{matrix_transpose}")

            product_matrix = product(matrix_A, matrix_B)
            product_hadamard = hadamard_product(matrix_A, matrix_B)
            if product_matrix is not None:
                print(f"Tích hai ma trận:\n{product_matrix}")
            else:
                print("Khong co tich ma tran")

            if product_hadamard is not None:
                print(f"Tích hadamard:\n{product_hadamard}")
            else:
                print("Khong co tich Hadamard")

            index = int(input("Nhập chỉ mục cột thay thế cột trong ma trận A: "))

            while is_out_of_column_range(matrix_A, index):
                index = int(input("Nhập lại chỉ mục cột: "))

            replace_col_A = replace_col(matrix_A, index)

            print(f"Ma trận A sau khi thay thế cột:\n{replace_col_A}")

            index = int(input("Nhập chỉ mục cột thay thế cột trong ma trận B: "))

            while is_out_of_column_range(matrix_B, index):
                index = int(input("Nhập lại chỉ mục cột: "))

            replace_col_B = replace_col(matrix_B, index)

            print(f"Ma trận B sau khi thay thế cột:\n{replace_col_B}")
            break
        except ValueError as e:
            print("Vui lòng nhập lại !")


if __name__ == "__main__":
    main()
