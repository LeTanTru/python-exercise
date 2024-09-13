def function_helper ( x ) :
2 if x > 0:
3 return ’T’
4 else :
5 return ’N’
6
7 def my_function ( data ) :
8 res = [ function_helper ( x ) for x in data ]
9 return res
10
11 data = [2 , 3 , 5 , -1]
12 print ( my_function ( data ) )
