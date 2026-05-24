def judge_number(n):

    for i in range(2, n):
        if n % i == 0:
            return False

    sum_val = 0
    while n > 0:
        sum_val += n % 10
        n //= 10

    if sum_val % 2 != 0:
        return False

    return True
    

a, b = map(int, input().split())

cnt = 0
for num in range(a, b+1):
    if judge_number(num):
        cnt += 1

print(cnt)