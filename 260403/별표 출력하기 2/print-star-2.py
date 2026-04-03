# 정수 N 입력받기
N = int(input())

for i in range(N, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()