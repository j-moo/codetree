n, m = map(int, input().split())
A = list(map(int, input().split()))

def solve():
    global m

    sum_val = 0

    while m >= 1:
        sum_val += A[m-1]

        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
    return sum_val

print(solve())