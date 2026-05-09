n = 5
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[0][i] = 1
    matrix[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()