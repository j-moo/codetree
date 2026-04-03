N = int(input())

cnt = 1
for i in range(1, N * 2):
    for j in range(cnt):
        print('*', end=' ')
    print()

    if i < N:
        cnt += 1
    else:
        cnt -= 1