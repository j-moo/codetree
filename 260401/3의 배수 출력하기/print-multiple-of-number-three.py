# N 입력받기
N = int(input())

# 1부터 N까지 3의 배수를 출력
i = 1
while i <= N:
    if i % 3 == 0:
        print(i, end=' ')
    i += 1