def make_arr(move):
    arr = [0]
    cur = 0

    for _ in range(move):
        v, t = map(int, input().split())

        for _ in range(t):
            cur += v
            arr.append(cur)

    return arr

n, m = map(int, input().split())

a = make_arr(n)
b = make_arr(m)

cnt = 0
prev = 0
cur = 0

for idx in range(len(a)):
    if a[idx] == b[idx]:
        cur = 0
    elif a[idx] > b[idx]:
        cur = 1
    else:
        cur = -1

    if cur != prev:
        cnt += 1
    
    prev = cur

print(cnt)