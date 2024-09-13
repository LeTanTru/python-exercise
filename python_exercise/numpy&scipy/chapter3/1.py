import numpy as np

dict_code = {
    "00": "'",
    "01": "`",
    "02": "?",
    "03": "~",
    "04": ".",
    "05": " ",
    "06": "A",
    "07": "Ă",
    "08": "Â",
    "09": "B",
    "10": "C",
    "11": "D",
    "12": "Đ",
    "13": "E",
    "14": "Ê",
    "15": "G",
    "16": "H",
    "17": "I",
    "18": "K",
    "19": "L",
    "20": "M",
    "21": "N",
    "22": "O",
    "23": "Ơ",
    "24": "Ô",
    "25": "P",
    "26": "Q",
    "27": "R",
    "28": "S",
    "29": "T",
    "30": "U",
    "31": "Ư",
    "32": "V",
    "33": "X",
    "34": "Y",
    "35": "không có mã",
}


def validate(A):
    try:
        inverse_matrix = np.linalg.inv(A)
        print("Ma trận này là khả nghịch.")

        return True
    except np.linalg.LinAlgError:
        print("Ma trận này không khả nghịch.")
        return False


def get_key(dict_code, val):
    return [
        int(key) - 5 if int(key) >= 5 else int(key) + 30
        for key, value in dict_code.items()
        if value == val
    ]


full_name = input("Nhập họ và tên: ")


# LÊ TÂ'N TRU.
A = np.array([[1, -2, 2], [-1, 1, 3], [1, -1, -4]])


def encrypt(full_name):
    if not validate(A):
        return
    encrypts = []

    n = len(full_name)
    if n % 3 != 0:
        full_name += " " * (3 - n % 3)
    n = len(full_name)
    origins = []
    i = 0
    for i in range(0, n - 2, 3):
        a = get_key(dict_code, full_name[i])
        b = get_key(dict_code, full_name[i + 1])
        c = get_key(dict_code, full_name[i + 2])
        origins.append(a + b + c)
    for origin in origins:
        origin_array = np.array(origin, dtype=int)
        encrypts.append(np.dot(origin_array, A))
    print(origins)
    return encrypts


def decrypt(encrypts):
    A_inv = np.linalg.inv(A)
    decrypts = []
    for encrypt in encrypts:
        decrypts.append(np.dot(encrypt, A_inv))
    full_name = ""
    for decrypt in decrypts:
        a = (decrypt[0] + 5) % 35
        b = (decrypt[1] + 5) % 35
        c = (decrypt[2] + 5) % 35
        full_name += (
            dict_code[str(int(a)) if a > 9 else "0" + str(int(a))]
            + dict_code[str(int(b)) if b > 9 else "0" + str(int(b))]
            + dict_code[str(int(c)) if c > 9 else "0" + str(int(c))]
        )
    return full_name


encrypts = encrypt(full_name)
decrypts = decrypt(encrypts)

print(encrypts)
print(decrypts)
