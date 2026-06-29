OFFSET = 100000
SIZE = 200005

n = int(input())

white_cnt = [0] * SIZE
black_cnt = [0] * SIZE
color = [0] * SIZE

# 1 = white
# 2 = black
# 3 = gray

cur = OFFSET

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'L':
        for idx in range(cur, cur - distance, -1):
            if color[idx] == 3:
                continue

            white_cnt[idx] += 1

            if white_cnt[idx] >= 2 and black_cnt[idx] >= 2:
                color[idx] = 3
            else:
                color[idx] = 1

        cur -= distance - 1

    else:
        for idx in range(cur, cur + distance):
            if color[idx] == 3:
                continue

            black_cnt[idx] += 1

            if white_cnt[idx] >= 2 and black_cnt[idx] >= 2:
                color[idx] = 3
            else:
                color[idx] = 2

        cur += distance - 1

white = 0
black = 0
gray = 0

for c in color:
    if c == 1:
        white += 1
    elif c == 2:
        black += 1
    elif c == 3:
        gray += 1

print(white, black, gray)