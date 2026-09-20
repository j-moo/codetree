def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0
d = 1

grid[x][y] = 1

for cnt in range(2, n * m + 1):
    nx = x + dx[d]
    ny = y + dy[d]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        d = (d + 1) % 4

    x = x + dx[d]
    y = y + dy[d]

    grid[x][y] = cnt

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()