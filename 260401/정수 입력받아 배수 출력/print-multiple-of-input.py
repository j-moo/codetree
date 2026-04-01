# N 입력받기
N = int(input())

# N의 배수 작은 것 부터 5개만 출력
for i in range(N, (N*5+1), N):
    print(i, end=' ')