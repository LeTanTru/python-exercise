m, y = map(int, input().split())
if m == 2:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(29)
    else:
        print(28)
    
