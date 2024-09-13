def function_helper (x , data ) :
    for i in data :
        if x == i :
            return 0

    return 1

def my_function ( data ) :
res = []
for i in data :
if function_helper (i , res ) :
res . append ( i )
