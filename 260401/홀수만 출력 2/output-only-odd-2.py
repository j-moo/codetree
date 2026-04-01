# 두 정수 입력받기
B, A = map(int, input().split())

# B이하 A이상 홀수 내림차순으로 출력
for i in range(B, A-1, -1):
    if i % 2 == 1:
        print(i, end=' ')