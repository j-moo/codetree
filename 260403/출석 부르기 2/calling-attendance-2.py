while True:
    # 정수 입력받기
    n = int(input())

    # 만약 번호가 1이면 John
    if n == 1:
        print('John')
    # 2이면 Tom
    elif n == 2:
        print('Tom')
    # 3이면 Paul
    elif n == 3:
        print('Paul')
    # 4이면 Sam
    elif n == 4:
        print('Sam')
    # 이외에는 Vacancy후 종료
    else:
        print('Vacancy')
        break