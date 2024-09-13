a, b, c = map(int, input().split())
if a == b == c:
    print(1)
elif a == b and a == c or b == a and b == c or c == a and c == b:
    print(2)
elif 

