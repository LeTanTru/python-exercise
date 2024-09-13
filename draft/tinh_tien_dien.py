levels = [1.678, 1.734, 2.014, 2.536, 2.834, 2.927]

def get_fee(n):
    total = 0
    if n <= 50:
        total = n * levels[0]
    elif n <= 100:
        total = 50 * levels[0] + (n - 50) * levels[1]
    elif n <= 200:
        total = 50 * levels[0] + 50 * levels[1] + (n - 100) * levels[2]
    elif n <= 300:
        total = 50 * levels[0] + 50 * levels[1] + 100 * levels[2] + (n - 200) * levels[3]
    elif n <= 400:
        total = 50 * levels[0] + 50 * levels[1] + 100 * levels[2] + 100 * levels[3] + (n - 300) * levels[4]
    else:
        total = 50 * levels[0] + 50 * levels[1] + 100 * levels[2] + 100 * levels[3] + 100 * levels[4] + (n - 400) * levels[5]
    return total

while True:
    try:
        n = float(input("Input electricity index: "))
        print(f"Total: {get_fee(n)}")
        break
    except:
        print("Invalid value !\nTry again !")

total = round(get_fee(n), 2)

print(total)
