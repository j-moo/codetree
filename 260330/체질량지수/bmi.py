# 키와 몸무게 입력받기
h, w = map(int, input().split())

# bmi구하고 출력
b = (10000 * w) / (h * h)
print(int(b))

# bmi가 25이상이라면  Obesity를 출력
if b > 25:
    print('Obesity')