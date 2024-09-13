def my_function ( data , max , min) :
    result = []
    for i in data :
        if i < min:
        result . append ( min )
    elif i > max :
    result . append ( max )
    else :
    result . append ( i )
    return result

my_list = [10 , 2 , 5 , 0 , 1]
max = 2
min = 1
print ( my_function (max = max , min = min , data = my_list ) )
