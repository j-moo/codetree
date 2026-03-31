# 세 정수 입력받기
a, b, c = map(int, input().split())

if a <= b < c:
    print(a)
elif a <= c < b:
    print(a)
elif b <= a < c:
    print(b)
elif b <= c < a:
    print(b)
elif c <= a < b:
    print(c)
elif c <= b < a:
    print(c)