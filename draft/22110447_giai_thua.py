import time


def giai_thua(n):
    if n == 1:
        return n
    return n * giai_thua(n - 1)


n = int(input("Nhập n: "))
res = [0] * (n + 2)


def giai_thua_khu_de_quy(n):
    if n == 1:
        return 1
    if res[n] != 0:
        return res[n]
    else:
        res[n] = n * giai_thua_khu_de_quy(n - 1)
    return res[n]


start = time.time()
print(f"Đệ quy: {giai_thua(n)}")
end = time.time()
print(f"Chạy trong: {end - start}")

# start = time.time()
# print(f"Khử đệ quy: {giai_thua_khu_de_quy(n)}")
# end = time.time()
# print(f"Chạy trong: {end - start}")
