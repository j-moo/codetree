pp, p = map(int, input().split())

print(pp, end=' ')

cnt = 2
while cnt <= 10:
    print(p, end=' ')

    pp, p = p, p + (2 * pp)
    cnt += 1