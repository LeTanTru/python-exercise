def my_function ( data , max , min) :
2 result = []
3 for i in data :
4 if i < min:
5 result . append ( min )
6 elif i > max :
7 result . append ( max )
8 else :
9 result . append ( i )
10 return result
11
12 my_list = [10 , 2 , 5 , 0 , 1]
13 max = 2
14 min = 1
15 print ( my_function (max = max , min = min , data = my_list ) )
