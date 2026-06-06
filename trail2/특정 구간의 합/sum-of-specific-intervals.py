n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def solve(a, b):
    sum_val = 0
    for i in range(a-1, b):
        sum_val += arr[i]
    print(sum_val)

for a, b in queries:
    solve(a, b)
