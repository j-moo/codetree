# 세 정수 입력받기
a, b, c = map(int, input().split())

# 첫 번째 수가 최소값이면 1 아니면 0
if a <= min(a, b, c):
    print(1, end=' ')
else:
    print(0, end=' ')

if a == b == c:
    print(1)
else:
    print(0)