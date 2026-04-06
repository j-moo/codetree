N = int(input())

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += 1
        print(2 * cnt, end=' ')
        if cnt == 4:
            cnt = 0
    print()