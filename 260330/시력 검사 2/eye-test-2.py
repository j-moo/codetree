# 시력 입력받기(실수)
a = float(input())

# 1.0 이상이면 High
# 0.5 이상이면 Middle
# 그 이외에는 Low 출력
if a >= 1.0:
    print('High')
elif a >= 0.5:
    print('Middle')
else:
    print('Low')