def my_function ( signal ) :
var = True
while var :
4 var = False
5 for i in range (len ( signal ) - 1) :
6 if signal [ i ] > signal [ i + 1]:
7 signal [ i ] , signal [ i + 1] = signal [ i + 1] , signal [ i ]
8 var = True
9
10 my_signal = [1 , 2 , 3 , 0]
11 my_function ( my_signal )
12 print ( my_signal )
