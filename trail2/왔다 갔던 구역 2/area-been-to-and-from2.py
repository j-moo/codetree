OFFSET = 1000

n = int(input())

arr = [0] * 2002
cur_idx = OFFSET

for _ in range(n):
    move, direction = input().split()
    move = int(move)

    if direction == 'L':
        next_idx = cur_idx - move

        arr[next_idx] += 1
        arr[cur_idx] -= 1

        cur_idx = next_idx

    else:
        next_idx = cur_idx + move

        arr[cur_idx] += 1
        arr[next_idx] -= 1

        cur_idx = next_idx

cnt = 0
prefix = 0

for i in range(len(arr)):
    prefix += arr[i]

    if prefix >= 2:
        cnt += 1

print(cnt)