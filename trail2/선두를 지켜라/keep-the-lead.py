n, m = map(int, input().split())

a = [0] * 1000001
b = [0] * 1000001

idx_a = 0
for _ in range(n):
    v, t = map(int, input().split())

    for _ in range(t):
        idx_a += 1
        a[idx_a] = a[idx_a - 1] + v

idx_b = 0
for _ in range(m):
    v, t = map(int, input().split())

    for _ in range(t):
        idx_b += 1
        b[idx_b] = b[idx_b - 1] + v


cnt = 0
prev = 0

for idx in range(1, idx_a + 1):
    if a[idx] > b[idx]:
        cur = 1
    elif a[idx] < b[idx]:
        cur = -1
    else:
        continue

    if prev != 0 and prev != cur:
        cnt += 1

    prev = cur

print(cnt)