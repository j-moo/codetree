# 4 * 4 배열
n = 4

matrix = [list(map(int, input().split())) for _ in range(n)]

# 각 줄의 합을 구해서 출력
for row in range(n):
    total = 0
    for number in range(n):
        total += matrix[row][number]
    print(total)