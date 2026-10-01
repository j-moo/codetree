def get_start(n, k):
    if k <= n:
        return 0, k - 1, 2
    if k <= 2 * n:
        return k - n - 1, n - 1, 3
    if k <= 3 * n:
        return n - 1, 3 * n - k, 0
    return 4 * n - k, 0, 1

n = int(input())
grid = [input().strip() for _ in range(n)]
k = int(input())

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

slash = [1, 0, 3, 2]    # /
backslash = [3, 2, 1, 0]  # \

x, y, direction = get_start(n, k)

count = 0

while 0 <= x < n and 0 <= y < n:
    count += 1

    if grid[x][y] == '/':
        direction = slash[direction]
    else:
        direction = backslash[direction]

    x = x + dx[direction]
    y = y + dy[direction]

print(count)