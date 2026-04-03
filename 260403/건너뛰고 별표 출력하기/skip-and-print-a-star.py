N = int(input())

cnt = 1
for i in range(1, 2 * N):
    for j in range(cnt):
        print('*', end='')
    print()
    print()

    if i < N:
        cnt += 1
    else:
        cnt -= 1