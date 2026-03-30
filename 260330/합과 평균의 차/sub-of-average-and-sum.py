# 세 정수 입력받기
a, b, c = map(int, input().split())

# 세 정수의 합, 평균, 합에서 평균을 뺀 값을 구하기
total = a + b + c
avg = total // 3
diff = total - avg

print(total)
print(avg)
print(diff)