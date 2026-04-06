N = int(input())

cnt = 10
for i in range(N):
    for j in range(N):
        cnt -= 1
        print(cnt, end='')
        if cnt == 1:
            cnt = 10
    print()