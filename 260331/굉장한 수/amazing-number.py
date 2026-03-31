# 자연수 N 입력받기
N = int(input())

if N % 2 == 1:
    if N % 3 == 0:
        print('true')
    else:
        print('false')
else:
    if N % 5 == 0:
        print('true')
    else:
        print('false')