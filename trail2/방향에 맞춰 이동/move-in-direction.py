n = int(input())

# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

directions = ["E", "W", "S", "N"]

x = 0
y = 0

for _ in range(n):
    dir, move = input().split()
    move = int(move)

    dir = directions.index(dir)

    x += move * dx[dir]
    y += move * dy[dir]

print(x, y)