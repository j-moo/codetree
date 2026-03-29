# 두 정수 입력받기
a, b = map(int, input().split())

# 두 수의 합을 차로 나누 값을 반올림하여 소수점 둘째 자리까지 출력
total = a + b
diff = a - b
ans = total / diff

print(f'{ans:.2f}')