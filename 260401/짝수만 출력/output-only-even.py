# 두 정수 입력받기
A, B = map(int, input().split())

# A~B까지 짝수만 출력
while A <= B:
    if A % 2 == 0:
        print(A, end=' ')
    A += 1