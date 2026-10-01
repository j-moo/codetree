def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#초기위치, 초기위치 카운트 입력
x, y = 0, 0
grid[x][y] = 1

cnt = 1
direction = 2

for _ in range(n * m - 1):
    cnt += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if in_range(nx, ny) and grid[nx][ny] == 0:
        grid[nx][ny] = cnt
        x, y = nx, ny
        continue

    direction = (direction + 4 - 1) % 4
    nx = x + dx[direction]
    ny = y + dy[direction]

    grid[nx][ny] = cnt
    x, y = nx, ny

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()