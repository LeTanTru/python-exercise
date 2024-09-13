a, b, c, d = map(float, input().split())
point = (a + b + c * 2 + d * 3) / 7
if point >= 8:
    print("GIOI")
elif point >= 6.5:
    print("KHA")
elif point >= 5:
    print("TRUNG BINH")
else:
    print("YEU")

