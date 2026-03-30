# 물 온도 입력받기
temp = int(input())

# 0 미만일 경우 ice 출력
# 100 이상일 경우 vapor 출력
# 그 외의 경우 water 출력
if temp < 0:
    print('ice')
elif temp >= 100:
    print('vapor')
else:
    print('water')