# 정수 N 입력받기
N = int(input())

# N을 1부터 1, 2, 3, ... 순으로 나누었을 때 1이하가 되는 순간
# 나눗셈을 진행한 총 횟수
cnt = 0
i = 1
while i <= 5000:
    # 종료조건
    if N <= 1:
        break

    N //= i
    i += 1
    cnt += 1


print(cnt)