N, M = map(int, input().split())

matrix = [[0]*M for _ in range(N)]
num = 1

# 첫 번째 행의 각 열을 시작점으로
for col_start in range(M):
    r, c = 0, col_start
    while r < N and c >= 0:
        matrix[r][c] = num
        num += 1
        r += 1
        c -= 1
        
for row_start in range(1, N):
    r, c = row_start, M-1
    while r < N and c >= 0:
        matrix[r][c] = num
        num += 1
        r += 1
        c -= 1

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()