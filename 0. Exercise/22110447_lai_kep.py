P = float(input("Nhập số tiền gốc (VND): "))

r_nam = float(input("Nhập lãi suất hàng năm (%): "))
# Chuyển đổi lãi suất từ phần trăm sang thập phân
r = r_nam / 100

n = int(input("Nhập số lần lãi suất được tính trong một năm: "))

thang = int(input("Nhập tháng cần tính lãi: "))

# Tính số tiền lãi tại tháng được nhập
t = thang / 12
A = P * (1 + r / n) ** (n * t)
lai_tai_thang = A - P

# In kết quả
print(f"Số tiền lãi tại tháng {thang} là: {lai_tai_thang:.2f}VND")
