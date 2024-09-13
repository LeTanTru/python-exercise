"""
Lê Tấn Trụ (nhóm trưởng) - 22110447 - 100%
Nguyễn Hồng Phúc - 22110401 - 90%
Võ Thị Thu Tâm - 22110411 - 80%
"""

import pandas as pd

df_data_diem_thi = pd.read_excel("./data.xlsx", sheet_name="DiemThi")
df_data_nv = pd.read_excel("./data.xlsx", sheet_name="NV")
tong_diem = {}

for index, row in df_data_diem_thi.iterrows():
    cmnd = row["CMND"]
    diem_van = row["Văn CN"]
    diem_ls = row["Lịch sử CN"]
    diem_dia_ly = row["Địa lí CN"]

    if (
        not pd.isnull(diem_van)
        and not pd.isnull(diem_ls)
        and not pd.isnull(diem_dia_ly)
    ):
        total_diem = round(diem_van + diem_ls + diem_dia_ly, 2)

        if cmnd in tong_diem:
            tong_diem[cmnd] += total_diem
        else:
            tong_diem[cmnd] = total_diem

nguyen_vong_dict = {}

for index, row in df_data_nv.iterrows():
    cmnd = row["CMND"]
    nguyen_vong = row["Thứ tự NV"]
    ma_nganh = row["Mã ngành"]

    if cmnd in nguyen_vong_dict:
        nguyen_vong_dict[cmnd].append((nguyen_vong, ma_nganh))
    else:
        nguyen_vong_dict[cmnd] = [(nguyen_vong, ma_nganh)]


def stable_marriage(nguyen_vong, tong_diem):

    # Sap xep danh sach hoc sinh giam dan theo diem
    sorted_students = sorted(
        nguyen_vong.keys(), key=lambda x: tong_diem.get(x, 0), reverse=True
    )

    engagements = {}
    # Moi ma nganh chi co 80 hoc sinh
    remaining_slots = {ma_nganh: 80 for ma_nganh in df_data_nv["Mã ngành"].unique()}

    while sorted_students:
        # Lay ra hoc sinh co diem cao nhat
        student = sorted_students.pop(0)
        # Lay ra danh sach nguyen vong
        preferred_choices = nguyen_vong[student]

        for choice in preferred_choices:
            # Lay ra ma nganh
            ma_nganh = choice[1]
            # Neu ma nganh chua co' va nganh do van con slot
            if ma_nganh not in engagements.values() and remaining_slots[ma_nganh] > 0:
                engagements[student] = choice
                remaining_slots[ma_nganh] -= 1
                break
            else:
                # Lay ra cac hoc sinh co cung ma nganh
                current_students = [
                    k for k, v in engagements.items() if v[1] == ma_nganh
                ]

                # Neu co hoc sinh co cung ma nganh
                if current_students:
                    # Lay ra  hoc sinh co diem thap nhat
                    lowest_ranked_student = min(
                        current_students, key=lambda x: tong_diem.get(x, 0)
                    )

                    # Kiem tra xem diem cua hoc sinh hien tai co lon hon diem thap nhat da tam trung tuyen
                    if tong_diem.get(student, 0) > tong_diem.get(
                        lowest_ranked_student, 0
                    ):
                        # Xoa hoc sinh thap diem nhat ra khoi ma nganh
                        del engagements[lowest_ranked_student]
                        # Ghep cap hoc sinh voi (thu tu nguyen vong, ma nganh)
                        engagements[student] = choice
                        break
        else:
            continue

    return engagements


matches = stable_marriage(nguyen_vong_dict, tong_diem)

# for cmnd, (nguyen_vong, ma_nganh) in matches.items():
#     print(
#         f"Thí sinh với CMND {cmnd} được ghép với nguyện vọng {nguyen_vong} và mã ngành {ma_nganh}"
#     )

# trung_tuyen_count = {}

# for _, (nguyen_vong, ma_nganh) in matches.items():
#     trung_tuyen_count[ma_nganh] = trung_tuyen_count.get(ma_nganh, 0) + 1
# total = 0

# for ma_nganh, count in trung_tuyen_count.items():
#     total += count
#     print(f"Mã ngành {ma_nganh}: {count} sinh viên trúng tuyển")
# print(f"Có tổng cộng {total} học sinh trúng tuyển.")

students_by_major = {}

for cmnd, (nguyen_vong, ma_nganh) in matches.items():
    if ma_nganh in students_by_major:
        students_by_major[ma_nganh].append(cmnd)
    else:
        students_by_major[ma_nganh] = [cmnd]

for ma_nganh, danh_sach_hs in students_by_major.items():
    print(f"Mã ngành {ma_nganh}:")
    for cmnd in danh_sach_hs:
        print(f"- Thí sinh với CMND {cmnd}")
