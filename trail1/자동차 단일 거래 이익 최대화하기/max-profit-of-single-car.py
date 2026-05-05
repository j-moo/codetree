N = int(input())
arr = list(map(int, input().split()))

max_val = 0
for i in range(N):
    for j in range(i+1, N):
        sum_val = arr[j] - arr[i]
        if sum_val > 0 and max_val < sum_val:
            max_val = sum_val

print(max_val)