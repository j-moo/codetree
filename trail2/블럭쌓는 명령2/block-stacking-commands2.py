n, k = map(int, input().split())

arr = [0] * (n + 1)

for i in range(k):
    a, b = map(int, input().split())

    for idx in range(a, b + 1):
        arr[idx] += 1

print(max(arr))