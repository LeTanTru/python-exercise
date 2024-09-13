def check_the_number ( N ) :
list_of_numbers = []
result = ""
for i in range (1 , 5) :
list_of_numbers . append ( i )
if N in list_of_numbers :
7 results = " True "
8 if N not in list_of_numbers :
9 results = " False "
10 return results
11
12 N = 2
13 results = check_the_number ( N )
14 print ( results )
