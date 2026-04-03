# N 입력받기
N = int(input())

x = 0
while True:
    # 종료조건
    if N == 1:
        break
    
    N //= 2
    x += 1

print(x)