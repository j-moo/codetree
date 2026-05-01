N = 10
arr = list(map(int, input().split()))

sum_val = 0
cnt = 0
for i in range(N):
    if arr[i] >= 250:
        break
    sum_val += arr[i]
    cnt += 1

avg = sum_val / cnt

print(f'{sum_val} {avg:.1f}')