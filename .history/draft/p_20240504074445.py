def my_function ( signal ) :
var = True
while var :
var = False
for i in range (len ( signal ) - 1) :
if signal [ i ] > signal [ i + 1]:
signal [ i ] , signal [ i + 1] = signal [ i + 1] , signal [ i ]
var = True

my_signal = [1 , 2 , 3 , 0]
my_function ( my_signal )
print ( my_signal )
