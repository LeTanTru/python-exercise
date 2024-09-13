def cholesky_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                sum_val = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = (matrix[i][i] - sum_val) ** 0.5  # Sửa thành căn bậc hai
            else:
                sum_val = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - sum_val) / L[j][j]

    return L

def nhap_ma_tran():
    while True:
        try:
            n = int(input("Nhập kích thước của ma trận: "))
            if n <= 0:
                print("Vui lòng nhập một số nguyên dương.")
                continue
            matrix = []
            print("Nhập các phần tử của ma trận theo từng hàng:")
            for _ in range(n):
                row = list(map(int, input().split()))
                if len(row) != n:
                    print("Đầu vào không hợp lệ. Vui lòng nhập chính xác", n, "phần tử.")
                    break
                matrix.append(row)
            if len(matrix) == n:
                return matrix
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng chỉ nhập số nguyên.")

# Sử dụng ví dụ
while True:
    matrix = nhap_ma_tran()
    L = cholesky_decomposition(matrix)
    print("\nKết quả phân tích Cholesky:")
    for row in L:
        print(row)
    choice = input("Bạn có muốn thực hiện phân tích Cholesky trên ma trận khác không? (có/không): ").lower()
    if choice != 'có':
        break
