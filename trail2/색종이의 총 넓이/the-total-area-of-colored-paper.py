OFFSET = 100
MAX_R = 201

n = int(input())
grid = [[0] * MAX_R for _ in range(MAX_R)]
rects = []

for _ in range(n):
    x1, y1 = map(int, input().split())
    rects.append([x1, y1])

for x1, y1 in rects:
    for i in range(x1 + OFFSET, x1 + OFFSET + 8):
        for j in range(y1 + OFFSET, y1 + OFFSET + 8):
            grid[i][j] = 1

cnt = 0

for row in grid:
    for elem in row:
        if elem == 1:
            cnt += 1

print(cnt)