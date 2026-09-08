n = int(input())

prev = int(input())

cnt = 1
max_cnt = 1

for i in range(n-1):
    cur = int(input())

    if cur * prev < 0:
        cnt = 1
    else:
        cnt += 1
    
    prev = cur
    max_cnt = max(max_cnt, cnt)

print(max_cnt)