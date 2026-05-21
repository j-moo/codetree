def solve(n):
    sum_val = 0
    for num in range(1, n+1):
        sum_val += num
    
    sum_val //= 10
    print(sum_val)

n = int(input())
solve(n)