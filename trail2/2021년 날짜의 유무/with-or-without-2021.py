def solve(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m > 12:
        return False
    else:
        if days[m] < d:
            return False
    return True

m, d = map(int, input().split())

if solve(m, d):
    print('Yes')
else:
    print('No')