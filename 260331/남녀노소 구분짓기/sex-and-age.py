# 성별 입력받기 남자면 0, 여자는 1
s = int(input())

# 나이 입력받기
a = int(input())

if a >= 19:
    if s == 0:
        print('MAN')
    else:
        print('WOMAN')
else:
    if s == 0:
        print('BOY')
    else:
        print('GIRL')