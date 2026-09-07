OFFSET = 100
MAX_R = 201

n = int(input())
grid = [[0] * MAX_R for _ in range(MAX_R)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    x2 += OFFSET
    y1 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            if i % 2 == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 2

cnt = 0
for row in grid:
    for elem in row:
        if elem == 2:
            cnt += 1

print(cnt)