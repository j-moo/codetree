arr_1 = [list(map(int, input().split())) for _ in range(3)]
null = input()
arr_2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        prod = arr_1[i][j] * arr_2[i][j]
        print(prod, end=' ')
    print()