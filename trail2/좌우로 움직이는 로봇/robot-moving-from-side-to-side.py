def get_position(commend_count):
    position = [0]
    current = 0

    for _ in range(commend_count):
        time, direction = input().split()
        time = int(time)

        move = -1 if direction == 'L' else 1

        for _ in range(time):
            current += move
            position.append(current)

    return position

n, m = map(int, input().split())

a = get_position(n)
b = get_position(m)

max_time = max(len(a), len(b))

a.extend([a[-1]] * (max_time - len(a)))
b.extend([b[-1]] * (max_time - len(b)))

answer = 0

for time in range(1, max_time):
    if a[time] == b[time] and a[time - 1] != b[time - 1]:
        answer += 1

print(answer)