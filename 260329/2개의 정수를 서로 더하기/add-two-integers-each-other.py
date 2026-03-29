# 두 개의 정수 입력받기
a, b = map(int, input().split())

# b를 a레 더하기
a += b

# a를 b에 더하기
b += a

print(a, b)