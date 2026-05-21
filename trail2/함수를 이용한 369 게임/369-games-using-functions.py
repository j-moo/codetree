def in_range(num):
    num = str(num)

    for i in num:
        if int(i) == 3 or int(i) == 6 or int(i) == 9:
            return True
    return False

def magic_num(num):
    return num % 3 == 0 or in_range(num)

a, b = map(int, input().split())

cnt = 0
for num in range(a, b+1):
    if magic_num(num):
        cnt += 1

print(cnt)