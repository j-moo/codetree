# 정수 N 입력받기
N = int(input())

# 점수에 따라 등급 출력
if N >= 90:
    print('A')
elif N >= 80:
    print('B')
elif N >= 70:
    print('C')
elif N >= 60:
    print('D')
else:
    print('F')