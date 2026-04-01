# 두 정수 입력받기
A, B = map(int, input().split())

# 두 정수 사이 홀수출력
for i in range(A, B+1):
    if i % 2 == 1:
        print(i, end=' ')