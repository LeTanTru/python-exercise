def function_helper ( x ) :
if x > 0:
return ’T’
else :
return ’N’

7 def my_function ( data ) :
8 res = [ function_helper ( x ) for x in data ]
9 return res
10
11 data = [2 , 3 , 5 , -1]
12 print ( my_function ( data ) )
