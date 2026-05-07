N, M = map(int, input().split())

# Please write your code here.
arr_2d = [[0] * M for _ in range(N)]

cnt = 0
for i in range(M):
    if i % 2 == 0:
        for j in range(N):
            arr_2d[j][i] = cnt
            cnt += 1
    else:
        for j in range(N-1, -1, -1):
            arr_2d[j][i] = cnt
            cnt += 1

for arr in arr_2d:
    for elem in arr:
        print(elem, end=' ')
    print()