def find_gcd(n, m):
    gcd = 0

    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    
    print(gcd)

n, m = map(int, input().split())

find_gcd(n, m)