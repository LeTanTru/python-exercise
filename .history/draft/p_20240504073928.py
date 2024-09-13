def my_function (x , y ) :
2 x . extend ( y)
3 return x
4
5 list_num1 = [1 , 2]
6 list_num2 = [3 , 4]
7 list_num3 = [0 , 0]
8
9 my_function ( list_num1 , my_function ( list_num2 , list_num3 ) )
