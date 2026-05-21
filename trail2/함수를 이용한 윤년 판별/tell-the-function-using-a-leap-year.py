def is_year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        return True
    return False

y = int(input())

if is_year(y):
    print('true')
else:
    print('false')