dict_day_of_weeks = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
}

dict_day_of_doomsday_of_first_of_centery = {
    8: [1700, 2100, 2500],
    3: [1600, 2000, 2400],
    4: [1500, 1900, 2300],
    6: [1800, 2200],
}


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def get_doomsday_of_first_year_of_centery(year):
    _year = int(year)
    for key in dict_day_of_doomsday_of_first_of_centery:
        if _year in dict_day_of_doomsday_of_first_of_centery[key]:
            return key


def get_day_of_date_duplicated_with_doomsday(month, year):
    if month % 2 == 0:
        if month != 2:
            return month
        elif is_leap_year(year):
            return 29
        else:
            return 28
    elif month == 1:
        if is_leap_year(year):
            return 4
        else:
            return 3
    elif month == 3:
        return 7
    elif month == 5:
        return 9
    elif month == 9:
        return 5
    elif month == 11:
        return 7
    elif month == 7:
        return 11


def get_doomsday_of_year(day, month, year):
    _day, _month, _year = int(day), int(month), int(year)
    xy = int(year[-2:])
    a = xy // 12
    b = xy % 12
    c = b // 4
    d = a + b + c
    e = d % 7

    doomsday_of_year = get_doomsday_of_first_year_of_centery(
        _year - xy
    )  # Lấy ra thứ của doomsday của năm đầu thế kỷ

    # print(dict_day_of_weeks[doomsday_of_year])

    doomsday_by_month = get_day_of_date_duplicated_with_doomsday(
        _month, _year
    )  # Lấy ra ngày trùng doomsday của tháng hiện tại

    day_of_doomsday_by_month = (
        doomsday_of_year + e
    )  # Thứ của ngày trùng doomsday của tháng hiện tại

    diff = _day - doomsday_by_month

    return dict_day_of_weeks[(diff + day_of_doomsday_by_month) % 7]


while True:
    try:
        date = input("Enter a date: (dd/MM/yyyy) or q to quit: ")
        if date == "q":
            break
        [day, month, year] = date.split("/")
        print([date, get_doomsday_of_year(day, month, year)])
    except:
        print("Invalid date !\nTry again !")
