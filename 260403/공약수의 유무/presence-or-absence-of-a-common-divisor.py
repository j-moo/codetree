# 두 정수 입력받기
A, B = map(int, input().split())

satisfied = 0
for i in range(A, B+1):
    if 1920 % i == 0 and 2880 % i == 0:
        satisfied = 1
    
print(satisfied)