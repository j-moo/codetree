# 입력으로 몇 개의 정수가 주어질 지 모른다 while문 사용

while True:
    # 입력값 받기
    n = int(input())

    # 입력값이 25라면 good을 출력하고 종료
    if n == 25:
        print('Good')
        break

    # 입력값이 25 보다 작다면 Higher출력
    elif n <= 25:
        print('Higher')
    
    # 그렇지 않다면(25보다 크다면) Lower출력
    else:
        print('Lower')