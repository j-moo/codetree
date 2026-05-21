def magic_number(n):
    if n % 2 == 0:
        num = 0
        while n > 0:
            num += n % 10
            n //= 10
        if num % 5 == 0:
            return True
    return False

n = int(input())

if magic_number(n):
    print('Yes')
else:
    print('No')