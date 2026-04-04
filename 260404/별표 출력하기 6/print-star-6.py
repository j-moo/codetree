N = int(input())

space = 0
cnt = 2 * N - 1
for i in range(2 * N - 1):
    for j in range(space):
        print(' ', end='')
    
    for k in range(cnt):
        print('*', end=' ')

    if i < N - 1:
        space += 2
        cnt -= 2
    else:
        space -= 2
        cnt += 2

    print()