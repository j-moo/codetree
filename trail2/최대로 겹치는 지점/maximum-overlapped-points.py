n = int(input())
segments = tuple(map(int, input().split()) for _ in range(n))

arr = [0] * 101

for a, b in segments:
    for idx in range(a, b + 1):
        arr[idx] += 1

print(max(arr))