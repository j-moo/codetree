def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
direction = 1
cnt = 65
grid[x][y] = chr(cnt)

for _ in range(n * m - 1):
    cnt += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
    
    if cnt > 90:
        cnt = 65
    grid[nx][ny] = chr(cnt)
    x, y = nx, ny

for row in grid:
    print(*row)