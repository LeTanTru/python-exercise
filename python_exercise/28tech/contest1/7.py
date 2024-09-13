a,b = map(int, input().split())
max_a = a // b * b
min_a = a // b * b + b
print(max_a)
print(min_a)
