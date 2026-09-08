n = int(input())

prev = int(input())
cnt = 1
max_cnt = 1

for _ in range(n - 1):
    num = int(input())

    if num == prev:
        cnt += 1
    else:
        cnt = 1

    max_cnt = max(max_cnt, cnt)
    prev = num

print(max_cnt)