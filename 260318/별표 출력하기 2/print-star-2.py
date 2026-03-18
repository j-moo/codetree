# 정수 N 입력받기
N = int(input())

# 왼쪽으로 정렬된 N높이만큼의 역삼각형 만들기
for i in range(N):
    for j in range(N - i):
        print('*', end=' ')
    print()
