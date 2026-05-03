arr = list(map(int, input().split()))

count_arr = [0] * 10

for elem in arr:
    if elem == 0:
        break

    number = elem // 10
    count_arr[number] += 1

for i in range(1, 10):
    print(f'{i} - {count_arr[i]}')
