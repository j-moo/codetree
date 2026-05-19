def min_num(n, m):
    num = max(n, m)
    
    while True:

        if num % n == 0 and num % m == 0:
            break
        
        num += 1
    return num

n, m = map(int, input().split())

print(min_num(n, m))