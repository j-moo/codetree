N = int(input())
arr_2d = [[0] * N for _ in range(N)]

num = 1
for i in range(N):
    for j in range(N):
        arr_2d[j][i] = num
        num += 1

for arr in arr_2d:
    for elem in arr:
        print(elem, end=' ')
    print()