my_list = [0 , 1 , 1 , 2 , 1]
odd = 1
even = 0

for number in my_list :
    if number % 2 == 0:
        odd += number
    else :
    even += number
print ( f" odd :{ odd} , even :{ even }")
