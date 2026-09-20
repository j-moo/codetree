s = list(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
d = 0
time = 0
answer = -1

for dir in s:
    time += 1

    if dir == 'L':
        d = (d - 1) % 4
    elif dir == 'R':
        d = (d + 1) % 4
    else:
        x = x + dx[d]
        y = y + dy[d]
        
        if x == 0 and y == 0:
            answer = time
            break

print(answer)