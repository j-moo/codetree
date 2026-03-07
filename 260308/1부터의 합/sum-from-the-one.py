# 정수 N 입력받기
N = int(input())

# 정수의 합을 저장할 변수 지정
num_sum = 0

# 1 부터 100까지 순회하며 1씩 증가
for i in range(1, 101):
    num_sum += i

    # 만약 num_sum가 입력값 N 보다 크다면 순회를 중단 하고 마지막에 더해진 수 출력g
    # 더 이상 순회할 필요 없음으로 break
    if num_sum > N:
        print(i)
        break