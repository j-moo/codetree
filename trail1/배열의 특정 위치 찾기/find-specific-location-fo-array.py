N = 10
arr = list(map(int, input().split()))

even_sum = 0
multiple_sum = 0
multiple_cnt = 0
for idx in range(1, N+1):
    if idx % 2 == 0:
        even_sum += arr[idx-1]

    if idx % 3 == 0:
        multiple_sum += arr[idx-1]
        multiple_cnt += 1

mumtiple_avg = multiple_sum / multiple_cnt

print(f'{even_sum} {mumtiple_avg:.1f}')