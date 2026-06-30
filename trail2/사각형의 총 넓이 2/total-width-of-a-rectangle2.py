OFFSET = 100

n = int(input())

grid = [[0] * 201 for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1

count = 0

for x in range(201):
    for y in range(201):
        count += grid[x][y]

print(count)