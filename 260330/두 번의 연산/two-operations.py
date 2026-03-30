# 정수 A 입력받기
A = int(input())

# A가 홀수라면 3을 더하기
if A % 2 == 1:
    A += 3

# A가 3의 배수라면 3으로 나누기
if A % 3 == 0:
    A //= 3

print(A)