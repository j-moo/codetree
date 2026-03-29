# 가로, 세로 길이를 입력받기
width, height = map(int, input().split())

# 가로 길이 8 증가시키기
width += 8
print(width)

# 세로 길이 3배 하기
height *= 3
print(height)

# 넓이 출력하기
area = width * height
print(area)