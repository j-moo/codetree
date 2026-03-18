# 세로(행) N, 가로(열) M 입력받기
N, M = map(int, input().split())

# N x M *로채우기
for i in range(N):
    for j in range(M):
        print('*', end=' ') 
    print()