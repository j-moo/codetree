# N 입력받기
N = int(input())

# 정사각형 넓이 구하고 출력
area = N * N
print(area)

# N 이 5보다 작다면 tiny출력
if N < 5:
    print('tiny')