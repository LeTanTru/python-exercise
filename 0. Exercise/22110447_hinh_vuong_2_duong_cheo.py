size = int(input())

# Vẽ hình vuông rỗng
print("Hình vuông rỗng có 2 đường chéo:")
for i in range(size):
  for j in range(size):
    if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or i + j == size - 1:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()
