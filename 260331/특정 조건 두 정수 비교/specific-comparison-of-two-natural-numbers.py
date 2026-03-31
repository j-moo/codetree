# 두 정수 입력받기
A, B = map(int, input().split())

# 첫 번째 수가 작으면 1, 아니면 0
if A < B:
    print(1, end=' ')
else:
    print(0, end=' ')

# 같으면 1, 아니면 0
if A == B:
    print(1)
else:
    print(0)