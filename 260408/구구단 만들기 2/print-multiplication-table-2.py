A, B = map(int, input().split())

for i in range(2, 9 + 1):
    for j in range(B, A - 1, -1):
        if i % 2 == 0:
            print(f'{j} * {i} = {i * j}', end=' ')
            if j > A:
                print('/', end=' ')
    if i % 2 == 0:
        print()