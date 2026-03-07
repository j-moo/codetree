# A가 B보다 커지는 순간을 몇 번 반복하는지 정해져 있지 않음
# while문 사용

# A, B 입력 받기
A, B = map(int, input().split())

# A가 B보다 커지는 순간 반복 종료
while A <= B:
    # A를 출력
    print(A, end=' ')

    # A의 수가 홀수인 경우(2로 나눈 나머지가 1인 경우)
    if A % 2 == 1:
        # 2배가 된다
        A *= 2
    
    # 그렇지 않은 경우 3만큼 증가
    else:
        A += 3