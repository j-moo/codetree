N = int(input())

for i in range(N):
    for j in range(N):
        if i == 0 or (j % 2 == 1 and i <= j):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()