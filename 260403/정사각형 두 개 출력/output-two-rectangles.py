# 정수 N 입력받기
N = int(input())

for i in range(2):
    for x in range(N):
        for y in range(N):
            print('*', end='')
        print()
    print()