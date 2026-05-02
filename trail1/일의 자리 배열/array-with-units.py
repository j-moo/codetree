N = 10
arr = [0] * N

first, second = map(int, input().split())
arr[0] = first
arr[1] = second

for idx in range(2, N):
    elem = arr[idx-2] + arr[idx-1]
    arr[idx] = elem % 10

print(*arr)