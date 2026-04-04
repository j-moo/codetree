# N 입력받기
N = int(input())

for i in range(N):
    for j in range(i):
        print(' ', end=' ')
    
    for k in range((2 * N - 1) - (2 * i)):
        print('*', end=' ')
    
    print()