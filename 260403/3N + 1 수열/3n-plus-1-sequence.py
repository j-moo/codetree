# N 입력받기
N = int(input())

# 조건에 따라 N이 1이 될때까지 반복
cnt = 0
while True:
    # 종료조건
    if N == 1:
        break
    
    if N % 2 == 0:
        N //= 2
    else:
        N = (N * 3) + 1
    
    cnt += 1

print(cnt)