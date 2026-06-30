OFFEST = 100000

n = int(input())

tiles = [0] * (OFFEST * 2)

# gray = 0
# white = 1
# black = 2

cur = OFFEST

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'L':
        for idx in range(cur, cur - distance, -1):
            tiles[idx] = 1

        cur = cur - distance + 1

    else:
        for idx in range(cur, cur + distance):
            tiles[idx] = 2

        cur = cur + distance - 1

white, black = 0, 0
for tile in tiles:
    if tile == 1:
        white += 1
    elif tile == 2:
        black += 1

print(white, black)