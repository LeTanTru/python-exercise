import time


def fibonacci(n):
    if n == 1 or n == 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Nhập n: "))

res = [0] * (n + 2)


def fibonacci_khu_de_quy(n):
    if n == 1 or n == 2:
        return n
    if res[n] != 0:
        return res[n]
    else:
        res[n] = fibonacci_khu_de_quy(n - 1) + fibonacci_khu_de_quy(n - 2)
    return res[n]


start = time.time()
print(f"Đệ quy: {fibonacci(n)}")
end = time.time()
print(f"Chạy trong: {end - start}")

# start = time.time()
# print(f"Khử đệ quy: {fibonacci_khu_de_quy(n)}")
# end = time.time()
# print(f"Chạy trong: {end - start}")
