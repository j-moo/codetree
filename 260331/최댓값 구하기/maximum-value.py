# 3개의 정수 입력받기
a, b, c = map(int, input().split())

if a <= b:
    if b <= c:
        print(c)
    else:
        print(b)
elif a <= c:
    if c <= b:
        print(b)
    else:
        print(c)
else:
    print(a)