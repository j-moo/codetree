s = list(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cur_dir = 0

x = 0
y = 0

for dir in s:
    if dir == 'F':
        x += dx[cur_dir]
        y += dy[cur_dir]
    elif dir == "L":
        cur_dir = (cur_dir -1 + 4) % 4
    else:
        cur_dir = (cur_dir + 1) % 4

print(x, y)    