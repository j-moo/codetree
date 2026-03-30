# 정수 입력받기
N = int(input())

# 점수가 80점 이상이면 pass출력
# 80점 미만이면 80점까지 필요한 점수 'x more score'출력
if N >= 80:
    print('pass')
else:
    print(f'{80 - N} more score')