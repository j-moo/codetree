def get_positions(command_count):
    positions = [0]
    current = 0

    for _ in range(command_count):
        direction, time = input().split()
        time = int(time)

        move = -1 if direction == 'L' else 1

        for _ in range(time):
            current += move
            positions.append(current)

    return positions


n, m = map(int, input().split())

a = get_positions(n)
b = get_positions(m)

limit = min(len(a), len(b))

for time in range(1, limit):
    if a[time] == b[time]:
        print(time)
        break
else:
    print(-1)