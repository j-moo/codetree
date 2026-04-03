# 정수 N 입력받기
N = int(input())

satisfied = 'N'
for i in range(2, N):
    if N % i == 0:
        satisfied = 'C'

print(satisfied)