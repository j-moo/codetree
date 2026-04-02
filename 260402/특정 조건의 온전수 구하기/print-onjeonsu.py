# N 입력받기
N = int(input())

# 온전한 수 출력
for i in range(1, N+1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        continue
    else:
        print(i, end=' ')