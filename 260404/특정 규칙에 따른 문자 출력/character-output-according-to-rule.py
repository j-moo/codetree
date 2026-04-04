N = int(input())

cnt = 1
for i in range(2 * N - 1):
    if i < N - 1:
        for j in range((N - 1) * 2 - (2 * i)):
            print(' ', end='')
    
    for k in range(cnt):
        print('@', end=' ')

    if i < N - 1:
        cnt += 1
    else:
        cnt -= 1
    
    print()