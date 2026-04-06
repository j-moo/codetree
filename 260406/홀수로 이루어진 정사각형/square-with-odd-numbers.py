N = int(input())


for i in range(N):
    cnt = 9 + 2 * i
    for j in range(N):
        cnt += 2
        print(cnt, end=' ')
    print()