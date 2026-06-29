OFFSET = 100

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

matrix = [0] * 201

mn = 0
for a, b in segments:
    for i in range(a + OFFSET, b + OFFSET):
        matrix[i] += 1
        if mn < matrix[i]:
            mn = matrix[i]

print(mn)