N = 10
arr = list(map(int, input().split()))

count_arr = [0] * 6

for elem in arr:
    count_arr[elem-1] += 1

for i in range(1, 7):
    print(f'{i} - {count_arr[i-1]}')