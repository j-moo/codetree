# 정수 A 입력받기
A = int(input())

# 조건을 만족하지 않는 수 출력하기
for i in range(1, A+1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    elif (i // 8) % 2 == 0:
        continue
    elif (i % 7) < 4:
        continue
    else:
        print(i, end=' ')