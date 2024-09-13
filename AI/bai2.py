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


prices = input_dict("prices")
print("-" * 20)
stock = input_dict("stock")
print("-" * 20)
total_values = {fruit: prices[fruit] * stock.get(fruit, 0) for fruit in prices}

sorted_fruits = sorted(total_values, key=lambda x: total_values[x], reverse=True)

for fruit in sorted_fruits:
    print(f"{fruit}: {total_values[fruit]}")
