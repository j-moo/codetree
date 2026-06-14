N = int(input())

cnt = 0

def f(n):
    global cnt
    # 종료조건
    if n == 1:
        return 1
    
    if n % 2 == 0:
        cnt += 1
        return f(n // 2)
    else:
        cnt += 1
        return f(n // 3)

f(N)
print(cnt)