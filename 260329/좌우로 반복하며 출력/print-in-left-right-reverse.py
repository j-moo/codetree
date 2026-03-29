# N 입력받기
N = int(input())

# 짝수 행은 1 ~ N 까지 순차적으로 증가
# 홀수 앵은 N ~ 1 까지 순차적으로 감소
for i in range(N):
    cnt = 1
    for j in range(N):
        if i % 2 == 0:
            print(cnt + j, end='')
        else:
            print(cnt + N - 1 - j, end='')
    print()