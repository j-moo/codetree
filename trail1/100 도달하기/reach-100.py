pp = 1
p = int(input())

print(pp, end=' ')

while True:
    print(p, end=' ')

    if p >= 100:
        break

    pp, p = p, pp + p