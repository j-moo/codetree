a, b = map(int, input().split())

sum_val = a + b

cnt = 0
while sum_val > 0:
    if sum_val % 10 == 1:
        cnt += 1
    
    sum_val = sum_val // 10

print(cnt)