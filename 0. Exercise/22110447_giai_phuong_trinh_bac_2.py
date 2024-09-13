from math import sqrt
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
  if b == 0:
    if c == 0:
      print("Phương trình có vô số nghiệm !")
    else:
      print("Phương trình vô nghiệm !")
  else:
    print(f"Phương trình có nghiệm x = {-c / b:.2f}")
else :
  delta = b ** 2 - 4 * a * c
  if delta < 0:
    print("Phương trình vô nghiệm !")
  elif delta == 0:
    print(f"Phương trình có nghiệm kép x1 = x2 = {-b / (2 * a):.2f}")
  else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print(f"Phương trình có 2 nghiệm: x1 = {x1:.2f}, x2 = {x2:.2f}")