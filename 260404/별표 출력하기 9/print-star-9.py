N = int(input())

for i in range(N):
    for j in range((N - 1) * 2 - (2 * i)):
        print(' ', end='')
    
    for k in range(2 * i + 1):
        print('*', end=' ')
    
    print()