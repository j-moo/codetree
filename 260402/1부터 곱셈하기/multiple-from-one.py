# 정수 N 입력 받기
N = int(input())

# 1부터 10까지 반복
prod = 1
for i in range(1, 11):
    # 차례대로 곱하기
    prod *= i

    # 만약 수들의 곱이 N보다 이상이면 마지막 곱해진 수 출력하고 종료
    if prod >= N:
        print(i)
        break