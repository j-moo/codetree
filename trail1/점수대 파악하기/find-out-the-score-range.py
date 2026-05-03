arr = list(map(int, input().split()))

count_arr = [0] * 11

for elem in arr:
    if elem == 0:
        break

    score = elem // 10
    count_arr[score] += 1

for i in range(10, 0, -1):
    print(f'{i*10} - {count_arr[i]}')