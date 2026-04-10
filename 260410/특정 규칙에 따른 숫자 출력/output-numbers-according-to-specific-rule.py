N = int(input())

cnt = 0
for i in range(N):
    for j in range(N):
        if i <= j:
            cnt += 1
            print(cnt, end=' ')
        else:
            print(' ', end=' ')
            
        if cnt == 9:
            cnt = 0
    print()