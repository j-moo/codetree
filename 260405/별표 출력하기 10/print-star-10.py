N = int(input())

cnt_1 = 1
cnt_2 = N
for i in range(N * 2):
    if i % 2 == 0:
        for j in range(cnt_1):
            print('*', end=' ')
        cnt_1 += 1
    else:
        for j in range(cnt_2):
            print('*', end=' ')
        cnt_2 -= 1
    print()