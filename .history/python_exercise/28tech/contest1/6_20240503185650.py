n = int(input())                

if n % 2 != 0:
    print("NO")
else:
    print("YES")
if n % 15 !=0:
    print("NO")
else:
    print("YES")
if not (n % 3 == 0 and n % 7 != 0):
    print("NO")
else:
    print("YES")
if not (n % 3 == 0 or n % 7 == 0):
    print("NO")
else:
    print("YES")
if not (n > 30 and n < 50):
    print("NO")
else:
    print("YES")
if not (n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0)):
    print("NO")
else:
    print("YES")
last = n % 100
if any(last % i == 0 for i in range(2, last)):
    print("NO")
else:
    print("YES")
if not (n < 100 and n % 23 == 0):
    print("NO")
else:
    print("YES")
if  (n >= 10 and n <= 20):
    print("NO")
else:
    print("YES")
last = n % 10
if last % 3 != 0:
    print("NO")
else:
    print("YES")


