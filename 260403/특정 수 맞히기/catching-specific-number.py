while True:
    # 정수 입력받기
    n = int(input())

    # 정수가 25보다 작다면 Higher
    if n < 25:
        print('Higher')
    # 25보다 크다면 Lower
    elif n > 25:
        print('Lower')
    # 같다면 Good
    # 종료
    else:
        print('Good')
        break