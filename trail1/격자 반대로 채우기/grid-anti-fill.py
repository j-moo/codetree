N = int(input())
arr_2d = [[0] * N for _ in range(N)]

cnt = 1
reverse = 1
for i in range(N):
    for j in range(N):
        if reverse % 2 ==  1:
            arr_2d[N-j-1][N-i-1] = cnt
            cnt += 1
        else:
            arr_2d[j][N-i-1] = cnt
            cnt += 1
    reverse += 1
    
for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()