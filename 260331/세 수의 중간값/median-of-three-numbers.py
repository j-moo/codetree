# 세 정수 입력받기
A, B, C = map(int, input().split())

if B > A and B < C:
    print(1)
else:
    print(0)