# 정수 N 입력받기
N = int(input())

# 1부터 100까지 반복
sum_val = 0
for i in range(1, 101):
    # 1부터 계속 더하기
    sum_val += i

    # 만약 합한값이 N이상이 되는 순간 더해진 수 출력 후 종료
    if sum_val >= N:
        print(i)
        break
