OFFSET = 1000
SIZE = 2001

grid = [[0] * SIZE for _ in range(SIZE)]

for k in range(3):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1 + OFFSET, x2 + OFFSET):
        for j in range(y1 + OFFSET, y2 + OFFSET):
            if k < 2:
                grid[i][j] = 1
            else:
                grid[i][j] = 0

cnt = 0

for row in grid:
    for elem in row:
        if elem == 1:
            cnt += 1

print(cnt)