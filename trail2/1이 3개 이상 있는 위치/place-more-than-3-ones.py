def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1

        if cnt >= 3:
            answer += 1

print(answer)