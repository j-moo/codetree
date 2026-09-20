def in_range(nx, ny):
    return 1 <= nx <= n and 1 <= ny <= n

n, t = map(int, input().split())
r, c, d = input().split()

dir = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r = int(r)
c = int(c)
d = dir[d]

for _ in range(t):
    nr = r + dr[d]
    nc = c + dc[d]

    if not in_range(nr, nc):
        d = (d + 2) % 4
        continue
    
    r = nr
    c = nc

print(r, c)