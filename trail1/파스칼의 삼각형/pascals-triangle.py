n = int(input())
matrix = [[0] * n for _ in range(n)]

matrix[0][0] = 1

for i in range(1, n):
    for j in range(n):
        matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

for row in matrix:
    for elem in row:
        if elem != 0:
            print(elem, end=' ')
    print()