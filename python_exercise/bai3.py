"""
Nhóm 21:
Lê Tấn Trụ(Nhóm trưởng) - Bài 2 + Tổng hợp Code
Nguyễn Hồng Phúc - Bài 3
Võ Thị Thu Tâm - Bài 1
"""


def input_dic():
    dictionary = {}
    n = int(input("Nhập số lượng cặp (key, value): "))

    for i in range(n):
        key = input("Nhập key: ")
        value = int(input("Nhập value: "))
        dictionary[key] = value

    return dictionary


def merge_dic(A, B):
    C = {}
    for key, value in A.items():
        C[key] = value
    for key, value in B.items():
        if key in C:
            C[key] = max(C[key], value)
        else:
            C[key] = value
    return C


A = input_dic()
B = input_dic()
C = merge_dic(A, B)
print("Dictionary C:\n", C)
