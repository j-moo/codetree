N = int(input())

cnt_1 = N
cnt_2 = 1
for i in range(2 * N):
    if i % 2 == 0:
        for j in range(cnt_1):
            print('*', end=' ')
        cnt_1 -= 1
    else:
        for j in range(cnt_2):
            print('*', end=' ')
        cnt_2 += 1
    print()