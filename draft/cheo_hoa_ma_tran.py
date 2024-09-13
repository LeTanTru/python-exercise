import numpy as np


# Hàm nhân ma trận với một hằng số alpha
def multiply_matrix_const(A, alpha):
    B = [[A[i][j] * alpha for j in range(len(A[0]))] for i in range(len(A))]
    return B


# Trừ hai ma trận
def sub_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# Hàm nhân hai ma trận
def mul_matrix(A, B):
    if len(A[0]) != len(B):
        return None
    result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] = check_number(result[i][j] + A[i][k] * B[k][j])
    return result


# Hàm lấy ra một cột thứ i của ma trận
def get_col(A, i):
    col = []
    for j in range(len(A)):
        col.append(A[j][i])
    return col


# Hàm nhân vector với hằng số
def mul_vector_alpha(A, const):
    return [A[i] * const for i in range(len(A))]


# Hàm tạo ma trận đường chéo từ các giá trị trên đường chéo cho trước
def diagonal_Matrix(values):
    n = len(values)
    return [[0 if i != j else values[i] for j in range(n)] for i in range(n)]


# Hàm tạo ma trận đơn vị
def get_unit_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def gauss_elimination(A):
    rows, cols = len(A), len(A[0])  # Lấy số dòng, số cột ma trận A
    r = -1  # Lưu giữ dòng đã thực hiện
    for j in range(cols - 1):
        t, r = 0, r + 1  ##Co sua
        if r == rows:
            break
        for i in range(r, rows):  # Xác định cột trái nhất không chứa hoàn toàn số 0
            if A[i][j] == 0:
                t = t + 1
                if t == (rows - r):
                    j = j + 1
                    i = r
            if A[i][j] != 0:
                c = j
                break
        if A[r][c] == 0:  # Đổi chỗ 2 dòng nếu cần
            for k in range(r, rows):
                if A[k][c] != 0:
                    A[k], A[r] = A[r], A[k]
                    break
        for l in range(c, cols):  # Nhân với 1/a
            if A[r][l] != 0:
                a = A[r][l]
                break
        for m in range(c, cols):
            if A[r][m] == 0:
                A[r][m] = A[r][m] / 1
                continue
            A[r][m] = A[r][m] / a
        for i in range(r + 1, rows):  # Trừ các dòng
            if A[i][c] != 0:
                x = A[i][c]
                for n in range(c, cols):
                    A[i][n] = A[i][n] - A[r][n] * x
    return A


# Hàm cộng 2 vector
def add_vector(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(len(vector1))]


# Hàm cho 2 vector cột bằng nhau
def equal_col(B, k, vector):
    for i in range(len(B)):
        B[i][k] = vector[i]


# Hàm kiểm tra dòng toàn 0
def check_row_is_zero(B, i):
    for j in range(len(B)):
        if B[i][j] != 0:
            return False
    return True


# Hàm tạo ma trận bổ sung
def create_additional_matrix(A):
    n = len(A)
    result = [[0 if i == n else A[j][i] for i in range(n + 1)] for j in range(n)]
    return result


# Hàm lưu vector riêng
def private_vector(R, check, index):
    for i in range(len(R)):
        if check_row_is_zero(R, i) == False:
            index += 1
            for j in range(len(R)):
                check[j][index] = R[i][j]
    return index


def back_substitution(A):
    # Biện luận dòng toàn số 0:
    rows, cols = len(A), len(A[0])
    i = rows - 1
    while i >= 0:
        count = 0  # Đếm số số 0 trên dòng i
        for j in range(cols):
            if A[i][j] == 0:
                count = count + 1
            if (
                count == (cols - 1) and A[i][cols - 1] != 0
            ):  # Khi dòng gồm toàn số 0 của A mà hệ số vế phải (tự do) là số # 0 thì kết luận hệ vô nghiệm
                return None  # print("Hệ phương trình vô nghiệm")
            if count == cols:
                rows = rows - 1  # bỏ dòng gồm toàn số 0
        i = i - 1
    # Phép thế ngược
    # Vô số nghiệm: xuất ra từng nghiệm ở dạng chuỗi
    if cols - 1 > rows:  # "Hệ vô số nghiệm"
        B = [
            [0 for j in range(len(A))] for i in range(len(A))
        ]  # Lưu nghiệm x1,x2,x3,... của hệ
        i = rows - 1
        trace = [0] * (cols - 1)  # Đánh dấu đã đặt ẩn hay chưa
        while i >= 0:
            dem = 0  # Đếm số 0 trên dòng i từ trái->phải cho đến khi gặp hệ số # 0 đầu tiên thì dừng lại
            for j in range(cols - 1):
                if A[i][j] == 0:
                    dem = dem + 1
                if A[i][j] != 0:
                    break
            k = cols - 2  # Đặt ẩn
            t0 = 0
            while k >= dem:
                if k != dem:
                    if trace[k] == 1:
                        k = k - 1
                        continue
                    else:
                        B[t0][k] = 1
                        trace[k] = 1
                        t0 = t0 + 1
                else:
                    vector = [0] * len(B)
                    for m in range(k + 1, cols - 1):
                        col_B = get_col(B, m)
                        vector = add_vector(vector, mul_vector_alpha(col_B, -A[i][m]))
                    equal_col(B, k, vector)
                    trace[k] = 1  # Lưu vết đã tính xong x thứ k
                k = k - 1
            i = i - 1
        return B
    # "Hệ có nghiệm duy nhất"
    B = [0] * (cols - 1)
    i = rows - 1
    while i >= 0:
        s = 0
        j = cols - 1
        if A[i][i] == 1:
            for k in range(cols - 1):
                s = float("{:.2f}".format(s + A[i][k] * B[k]))
            B[i] = float("{:.2f}".format(A[i][cols - 1] - s))
        i = i - 1
    return B


# Hàm giải HPT (A-λI_n)X = 0
def solve_equations(A, lamda, n):
    B = sub_matrix(A, multiply_matrix_const(get_unit_matrix(n), lamda))
    R1 = gauss_elimination(B)  # Phép khử Gauss
    R = create_additional_matrix(R1)
    return back_substitution(R)  # Phép thế ngược


# Hàm kiểm tra sai số
import math


def check_number(number):
    if math.isclose(number, math.ceil(number), abs_tol=1e-20):
        return math.ceil(number)
    elif math.isclose(number, math.floor(number), abs_tol=1e-20):
        return math.floor(number)
    elif math.isclose(number, round(number, 2), abs_tol=1e-20):
        return round(number, 2)
    else:
        return number


# Hàm tìm ma trận nghịch đảo
def inverse(A):
    n = len(A)  # A là ma trận vuông cấp n
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Tạo ma trận đơn vị
    # Giải thuật với phép khử Gauss – Jordan
    for i in range(n):
        t = 0  # Biến đếm số số 0 từ dòng i đến dòng n trên cột i
        for j in range(i, n):  # Bước 1:
            if A[j][i] == 0:
                t = t + 1
        if t == (n - i):  # Nếu chúng gồm toàn số 0
            print("Ma trận không khả nghịch")
            return 0
        if A[i][i] == 0:  # Ngược lại đổi chỗ 2 dòng nếu cần thiết
            for k in range(i, n):
                if A[k][i] != 0:
                    A[k], A[i] = A[i], A[k]
                    I[k], I[i] = I[i], I[k]
                    break
        if A[i][i] != 0:  # Bước 2: Nhân với 1/a
            a = A[i][i]
        for m in range(n):
            A[i][m] = A[i][m] / a
            I[i][m] = I[i][m] / a
        for j in range(
            n
        ):  # Bước 3: Cộng một bội số thích hợp của dòng i với các dòng khác dòng i
            if (
                j == i
            ):  # để biến các số hạng trên cột i về số 0 (trừ số hạng nằm ở dòng i)
                continue
            if A[j][i] != 0:
                x = A[j][i]
                for k in range(n):
                    A[j][k] = A[j][k] - A[i][k] * x
                    I[j][k] = I[j][k] - I[i][k] * x
    for i in range(n):
        for j in range(n):
            I[i][j] = check_number(I[i][j])

    return I


# Hàm kiểm tra xem nếu có giá trị lamda lặp lại thì chỉ giữ lại 1 lamda
def check_different(vector):
    for i in range(len(vector)):
        for j in range(i + 1, len(vector)):
            if check_number(vector[i]) == check_number(vector[j]):
                vector[j] = -99999


def diagonalizable_matrix(A):
    n = len(A)
    w, v = np.linalg.eig(A)
    check_different(w)
    # Giải từng trị riêng
    check = [[0 for i in range(n)] for j in range(n)]
    index = -1
    for i in range(len(w)):
        lamda = round(w[i], 2)
        if lamda != -99999:
            R = solve_equations(A, lamda, n)
            index = private_vector(R, check, index)
    if index == n - 1:
        P = check
        P_inverse = inverse(P)  # Tính P^-1
        D0 = mul_matrix(P_inverse, A)
        P = inverse(P_inverse)
        D = mul_matrix(D0, P)
    else:
        print("Ma trận không chéo hóa được vì chỉ có", index + 1, "vector riêng")
        return None
    return P, D


A = [[3, 4, -4], [-2, -1, 2], [-2, 0, 1]]

if diagonalizable_matrix(A) != None:
    P, D = diagonalizable_matrix(A)
    print("- Ma trận chéo P:", P)
    print("- Suy ra P^(-1):", inverse(P), "\n- Ma trận đường chéo D:", D)
