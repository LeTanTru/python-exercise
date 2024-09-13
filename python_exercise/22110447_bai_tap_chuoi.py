def cau_1(s):
    for x in s:
        print(x, end=" ")


def cau_2(s):
    return s[::-1]


def cau_3(s, substr):
    return s.count(substr)


def cau_4(s):
    return s == s[::-1]


def cau_5(s):
    res = ""
    for x in s:
        if x not in res:
            res += x
    return res


def cau_6(s):
    res = ""

    for x in s:
        if x.islower():
            res += x.upper()
        elif x.isupper():
            res += x.lower()
        else:
            res += x

    return res


def cau_7(s):
    l = 0
    for _ in s:
        l += 1
    return l


def cau_8(s):
    chars = list(s)
    chars.sort()

    return "".join(chars)


def cau_9(s):
    start_index = 0
    max_length = 0
    res = ""

    index = {}

    for current_index, char in enumerate(s):
        if char in index and index[char] >= start_index:
            start_index = index[char] + 1

        index[char] = current_index

        current_length = current_index - start_index + 1

        if current_length > max_length:
            max_length = current_length
            res = s[start_index : current_index + 1]
    return res


def cau_10(s):
    res = s
    max_fre = -1
    for c in s:
        if s.count(c) > max_fre:
            max_fre = s.count(c)
            res = c
    return  res, max_fre


def cau_11(s):
    start_index = 0
    max_length = 0
    res = ""

    dict = {}

    for current_index, char in enumerate(s):
        if char in dict and dict[char] >= start_index:
            start_index = dict[char] + 1

        dict[char] = current_index

        current_length = current_index - start_index + 1

        if current_length > max_length:
            max_length = current_length
            res = s[start_index : current_index + 1]
    return res


def cau_12(s):
    return len(s.split(" "))


def cau_13(s1, s2):
    return s1 == s2[::-1]


def cau_14(s, char, new_char):
    return s.replace(char, new_char)


def cau_15(s, l):
    word = s.split(" ")
    res = []
    for w in word:
        if len(w) >= l:
            res.append(w)
    return res


def cau_16(s):
    start = 0
    max_length = 0
    current_length = 0
    char_index_map = {}
    longest_substring_start = 0

    for index, char in enumerate(s):
        if char not in char_index_map or char_index_map[char] < start:
            current_length += 1
        else:
            start = char_index_map[char] + 1
            current_length = index - start + 1

        char_index_map[char] = index

        if current_length > max_length:
            max_length = current_length
            longest_substring_start = start

    return s[longest_substring_start : longest_substring_start + max_length]


def cau_17(s):
    l = len(s)
    substr_list = set()

    for i in range(1, l + 1):
        for j in range(l - i + 1):
            substr = s[j : j + i]
            substr_list.add(substr)

    return list(substr_list)


def cau_18(s):
    l = len(s)
    repeated_substrings = set()

    for i in range(l):
        for j in range(l - i + 1):
            substr = s[i:j]
            if s.count(substr) >= 2 and substr not in repeated_substrings:
                repeated_substrings.add(substr)
    return list(sorted(repeated_substrings, key=len, reverse=True))


def cau_19(s):
    ascii_list = [ord(c) for c in s]
    string = "".join([chr(ascii) for ascii in ascii_list])

    return {"String to ascii": ascii_list, "Ascii to string": string}


def cau_20(s):
    digit = 0
    upper = 0
    lower = 0
    for c in s:
        if c.isdigit():
            digit += 1
        elif c.isupper():
            upper += 1
        elif c.islower():
            lower += 1

    return {
        "Digit": digit,
        "Upper": upper,
        "Lower": lower,
        "Special": len(s) - digit - upper - lower,
    }


# print(f"Cau_1: ", end=" ")
# cau_1("This is a string!")
# print(f"Cau_2: {cau_2("This is a string!")}")
# print(f"Cau_3: {cau_3("This is a string!", "is")}")
# print(f"Cau_4: {cau_4("abccba")}")
# print(f"Cau_5: {cau_5("This is a string!")}")
# print(f"Cau_6: {cau_6("ThIs iS A sTRiNG!")}")
# print(f"Cau_7: {cau_7("This is a string!")}")
# print(f"Cau_8: {cau_8("This is a string!")}")
# print(f"Cau_9: {cau_9("This is a string!")}")
# print(f"Cau_10: {cau_10("hello from python")}")
# print(f"Cau_11: {cau_11("This is a string!")}")
# print(f"Cau_12: {cau_12("This is a string!")}")
# print(f"Cau_13: {cau_13("This is a string!", "!gnirts a si sihT")}")
# print(f"Cau_14: {cau_14("This is a string!", "s", "S")}")
# print(f"Cau_15: {cau_15("This is a string!", 3)}")
# print(f"Cau_16: {cau_16("This is a string!")}")
# print(f"Cau_17: {cau_17("This is a string!")}")
# print(f"Cau_18: {cau_18("This is a string!")}")
# print(f"Cau_19: {cau_19("This is a string!")}")
# print(f"Cau_20: {cau_20("This is a string!")}")
