def input_dict(dict_name):
    while True:
        try:
            size = int(input(f"Input size of {dict_name}: "))
            break
        except ValueError:
            print("Value must be a number. ")

    dict = {}
    for i in range(size):
        key = input("Input key: ")
        while type(key) != str:
            key = input("Key must be a string: ")

        value = 0
        while True:
            try:
                value = float(input("Input value: "))
                break
            except ValueError:
                print("Value must be a number. ")
        dict[key] = value
    return dict


def merge(A, B):
    C = {}
    for key in A:
        if key not in B:
            C[key] = A[key]
        else:
            C[key] = max(A[key], B[key])

    for key in B:
        if key not in A:
            C[key] = B[key]

    return C


A = input_dict("A")
print("-" * 20)
B = input_dict("B")

C = merge(A, B)
print("-" * 20)
for key in C:
    print(f"{key}: {C[key]}")

# A = {
#     "Math": 10,
#     "Literature": 8,
#     "English": 7,
#     "Physics": 8.5,
#     "Chemistry": 10,
#     "Biology": 3,
# }

# B = {
#     "Math": 7,
#     "Literature": 9.5,
#     "English": 9,
#     "History": 9,
#     "Geography": 9.5,
#     "Civic Education": 8,
# }
