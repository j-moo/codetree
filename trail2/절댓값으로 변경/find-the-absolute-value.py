def make_abs(n, arr):
    for i in range(n):
        print(abs(arr[i]), end=' ')

n = int(input())
arr = list(map(int, input().split()))

make_abs(n, arr)