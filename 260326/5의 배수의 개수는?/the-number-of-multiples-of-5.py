# 4 * 4 배열
N = 4

# 2차원 배열 입력받기
matrix = [list(map(int, input().split())) for _ in range(N)]

# 5의 배수의 개수를 출력
cnt = 0
for row in matrix:
    for number in row:
        if number % 5 == 0:
            cnt += 1

print(cnt)