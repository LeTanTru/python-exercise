n = int(input())                
check = True
if n % 2 != 0 and n % 15 == 0 and (n % 3 == 0 and n % 7 !=0 ) and  (n%3==0 or n % 7==0):
    check = False
