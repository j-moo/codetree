# N 값 입력받기
N = int(input())

# N * N 2차원 배열 만들기
matrix = [[0] * N for _ in range(N)]

# 짝수열 1 ~ N 까지 순차적으로 증가
# 홀수열 N ~ 1 까지 순차적으로 감소
for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            matrix[j][i] = j + 1
        else:
            matrix[j][i] = N - j 

for row in matrix:
    for number in row:
        print(number, end='')
    print()