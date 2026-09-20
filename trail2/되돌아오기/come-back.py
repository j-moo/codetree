n = int(input())

dir = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3,
}

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
x = 0
y = 0
answer = -1

for _ in range(n):
    d, l = input().split()

    for _ in range(int(l)):
        x = x + dx[dir[d]]
        y = y + dy[dir[d]]
        time += 1

        if x == 0 and y == 0:
            answer = time
            break
    
    if answer != -1:
        break
    
print(answer)