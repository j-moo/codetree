arr = list(map(int, input().split()))

sum_val = 0
for idx in range(len(arr)):
    if arr[idx] == 0:
        sum_val += arr[idx-3] + arr[idx-2] + arr[idx-1]
        break

print(sum_val)