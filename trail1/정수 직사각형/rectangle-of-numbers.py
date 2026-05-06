N, M = map(int, input().split())
matrix = [[0] * M  for _ in range(N)]

num = 1
for i in range(N):
    for j in range(M):
        matrix[i][j] = num
        print(matrix[i][j], end=' ')
        num += 1
    print()