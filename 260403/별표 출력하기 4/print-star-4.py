N = int(input())

cnt = N
for i in range(1, N * 2):
    for j in range(cnt):
        print('*', end=' ')
    print()

    if i < N:
        cnt -= 1
    else:
        cnt += 1