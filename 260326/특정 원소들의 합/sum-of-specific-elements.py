# 4 * 4 이차원 배열
N = 4

# 2차원 배열 입력받기
matrix = [list(map(int, input().split())) for _ in range(N)]

# 색칠된 칸은 행이 한 칸 증가할수록 열의 개수가 왼쪽에서부터 하나씩 증가
# 색칠된 칸의 정수의 합을 출력
total = 0
for row in range(N):
    for number in range(row + 1):
        total += matrix[row][number]

print(total)