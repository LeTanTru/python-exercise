x, y = map(float, input().split())
res = x ** y if x == int(x) and y == int(y) else "{:2f}.format(x ** y)"
if type(res) == str:
    
