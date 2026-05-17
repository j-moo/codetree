n = int(input())

sum_val = 0
for _ in range(n):
    number = int(input())
    sum_val += number

sum_val = str(sum_val)
sum_val = sum_val[1:] + sum_val[0]
print(sum_val)