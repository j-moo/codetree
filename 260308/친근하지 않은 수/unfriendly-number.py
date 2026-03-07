# 정수 입력 받기
N = int(input())

# 친근하지 않은 수를 출력하기 위한 변수를 지정
cnt = 0

# 0 부터 N까지 순회
for i in range(0, N + 1):
    # 만약 친근한 수라면 다음 순회로 넘어간다.
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    # 그렇지 않다면 카운트 + 1
    else:
        cnt += 1

print(cnt)