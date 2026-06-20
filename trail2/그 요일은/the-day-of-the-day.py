m1, d1, m2, d2 = map(int, input().split())
day = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6,
}

start = sum(month[:m1]) + d1
end = sum(month[:m2]) + d2

total = end - start + 1

target = days[day]

answer = total // 7

if target < total % 7:
    answer += 1

print(answer)