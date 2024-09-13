def function_helper (x , data ) :
2 for i in data :
3 if x == i :
4 return 0
5
6 return 1
7
8 def my_function ( data ) :
9 res = []
10 for i in data :
11 if function_helper (i , res ) :
12 res . append ( i )
