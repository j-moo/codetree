# 두 정수 입력받기
a, b, c = map(int, input().split())

# c의 배수가 없다고 가정
satisfied = 'YES'
for i in range(a, b+1):
    if i % c == 0:
        satisfied = 'NO'

print(satisfied)