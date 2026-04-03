cnt = 0
while True:
    # 정수 입력받기
    n = int(input())

    # 짝수면 몫을 출력
    if n % 2 == 0:
        print(n // 2)
        # 카운팅 + 1
        cnt += 1
    
    # 카운팅이 3회가 되면 종료
    if cnt == 3:
        break