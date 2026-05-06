n = 4

for _ in range(n):
    arr = list(map(int, input().split()))

    sum_val = 0
    for i in arr:
        sum_val += i

    print(sum_val)