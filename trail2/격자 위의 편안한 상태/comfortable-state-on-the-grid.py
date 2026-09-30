def in_range(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

N, M = map(int, input().split())

grid = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    grid[x][y] = 1
    cnt = 0

    for dr, dc in zip(dx, dy):
        nx = x + dr 
        ny = y + dc

        if not in_range(nx, ny):
            continue
        
        if grid[nx][ny] == 0:
            continue

        cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)