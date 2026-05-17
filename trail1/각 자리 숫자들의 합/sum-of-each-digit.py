n = int(input())

sum_val = 0

while n > 0:
    sum_val += n % 10
    n = n // 10

print(sum_val)