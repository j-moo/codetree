# 정수 N 입력받기
N = int(input())

# 왼쪽으로 정렬된 깊이 N 삼각형 출력하기
# 단 줄이 늘어날 때 마다 * 은 2씩 증가
for i in range(N):
    for j in range(i * 2 + 1):
        print('*', end='')
    print()