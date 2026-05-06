matrix = [list(map(int, input().split())) for _ in range(2)]


total = 0
total_cnt = 0
for i in range(2):
    row_sum = 0
    row_cnt = 0
    for j in range(4):
        row_sum += matrix[i][j]
        row_cnt += 1
        total += matrix[i][j]
        total_cnt += 1
    
    row_avg = row_sum / row_cnt
    print(f'{row_avg:.1f}', end=' ')

print()

for i in range(4):
    col_sum = 0
    col_cnt = 0
    for j in range(2):
        col_sum += matrix[j][i]
        col_cnt += 1

    col_avg = col_sum / col_cnt
    print(f'{col_avg:.1f}', end=' ')

print()

total_avg = total / total_cnt
print(f'{total_avg:.1f}')