# 나이와 성별 입력받기
a = input().split()
b = input().split()

if int(a[0]) >= 19 or int(b[0]) >= 19:
    if a[1] == 'M' or b[1] == 'M':
        print(1)
    else:
        print(0)
else:
    print(0)