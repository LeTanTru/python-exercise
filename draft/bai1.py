"""
Nhóm 21:
Lê Tấn Trụ(Nhóm trưởng) - Bài 2 + Tổng hợp Code
Nguyễn Hồng Phúc - Bài 3
Võ Thị Thu Tâm - Bài 1
"""


def doi_tien():
    tien = float(input("Nhập số tiền cần đổi: "))

    # Kiểm tra số tiền có tròn không
    if tien % 1000 != 0:
        print("Số tiền không tròn, vui lòng nhập lại.")
        doi_tien()
        return

    # Mệnh giá của các tờ tiền
    menh_gia = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]

    # Đếm số tờ tiền cần đổi
    so_to = []
    for menh_gia_tien in menh_gia:
        so_to.append(int(tien / menh_gia_tien))
        tien = tien % menh_gia_tien

    # In ra kết quả
    for i in range(len(menh_gia)):
        if so_to[i] > 0:
            print(f"{so_to[i]} tờ {menh_gia[i]} VND")


doi_tien()
