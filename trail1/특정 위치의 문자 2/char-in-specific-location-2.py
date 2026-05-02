N = 10
arr = input().split()

for idx in range(N):
    if idx + 1 == 2 or idx + 1 == 5 or idx + 1 == 8:
        print(arr[idx], end=' ')