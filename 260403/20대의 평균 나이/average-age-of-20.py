avg = 0
sum_val = 0
cnt = 0
while True:
    age = int(input())
    
    if not 20 <= age < 30:
        break

    # 나이 평균 구하기
    sum_val += age
    cnt += 1
    avg = sum_val / cnt

print(f'{avg:.2f}')