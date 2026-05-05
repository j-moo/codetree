N = int(input())
arr = list(map(int, input().split()))

min_diff = 999
for i in range(N):
    for j in range(i+1, N):
        diff = abs(arr[i] - arr[j])
        if min_diff > diff:
            min_diff = diff

print(min_diff)