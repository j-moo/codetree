# A 분류된 인원을 세기 위한 변수
cnt = 0

# 3명씩 검사
for i in range(3):
    sig, temp = input().split()
    
    # A 분류하기
    if sig == 'Y' and int(temp) >= 37:
        cnt += 1

# 위급상황 판별
if cnt >= 2:
    print('E')
else:
    print('N')