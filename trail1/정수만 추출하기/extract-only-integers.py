arr = input().split()

answer = 0
for num in arr:
    sum_val = ''
    for elem in num:
        if not elem.isdigit():
            break
        
        sum_val += elem
    answer += int(sum_val)

print(answer)