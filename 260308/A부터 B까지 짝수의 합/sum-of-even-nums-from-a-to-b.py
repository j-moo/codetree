# A, B 입력 받기
A, B = map(int, input().split())

# 짝수의 합을 저장할 변수
total = 0

# A 부터 B 까지 순회
for i in range(A, B + 1):
    # 2로 나눈 나머지가 0 이라면 짝수이므로 해당 정수를 더해준다
    if i % 2 == 0:
        total += i

print(total)