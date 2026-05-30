Y, M, D = map(int, input().split())


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False

    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days[2] = 29

    if 1 <= day <= days[month]:
        return True

    return False


def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"


if is_valid_date(Y, M, D):
    print(get_season(M))
else:
    print(-1)