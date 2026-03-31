# 점수 입력받기
A, B = map(int, input().split())

if A >= 90:
    if B == 100:
        print(100000)
    elif B >= 90:
        print(50000)