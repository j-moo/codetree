N, M = map(int, input().split())
matrix = [[0] * N for _ in range(N)]

cnt = 1
for _ in range(M):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = cnt
    cnt += 1

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()