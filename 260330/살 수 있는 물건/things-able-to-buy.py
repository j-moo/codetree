#  가지고 있는 돈 입력받기
N = int(input())

# 살 수 있는 물건 중 가장 비싼 물건 출력
if N >= 3000:
    print('book')
elif N >= 1000:
    print('mask')
else:
    print('no')