# 두 정수 입력받기
B, A = map(int, input().split())

# B부터 A까지 짝수 내림차순으로 출력
while B >= A:
    if B % 2 == 0:
        print(B, end=' ')
    B -= 1