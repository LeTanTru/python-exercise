def function_helper ( x ) :
    if x > 0:
        return ơTơ
    else :
        return ơNơ

def my_function ( data ) :
    res = [ function_helper ( x ) for x in data ]
    return res

data = [2 , 3 , 5 , -1]
print ( my_function ( data ) )
