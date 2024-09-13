n = int(input())                
check = True
if n % 2 != 0:
    check = False
if n % 15 !=0:
    check = False
if not (n % 3 == 0 and n % 7 != 0):
    check = False
if not (n % 3 == 0 or n % 7 == 0):
    check = False
if not (n > 30 and n < 50):
    check = False
if not (n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0)):
    check = False
if not ()
