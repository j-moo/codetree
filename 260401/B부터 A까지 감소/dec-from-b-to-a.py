# 두 정수 입력받기
A, B = map(int, input().split())

# B부터 A까지 1씩 감소하며 출력
for i in range(B, A-1, -1):
    print(i, end=' ')