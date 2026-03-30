# 두 정수 입력받기
a, b = map(int, input().split())

# a 가 b 보다 크다면 두 수의 곱을 출력
# 그렇지 않다면 b를 a로 나눈 몫을 출력
if a > b:
    print(a * b)
else:
    print(b // a)