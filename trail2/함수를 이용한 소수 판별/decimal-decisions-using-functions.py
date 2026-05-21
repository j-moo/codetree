def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())

sum_val = 0
for num in range(a, b+1):
    if is_prime(num):
        sum_val += num

print(sum_val)