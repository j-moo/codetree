N = int(input())
arr = list(map(float, input().split()))

sum_val = 0
cnt = 0
for elem in arr:
    sum_val += elem
    cnt += 1

avg = sum_val / cnt

grade = ''
if avg >= 4.0:
    grade = 'Perfect'
elif avg >= 3.0:
    grade = 'Good'
else:
    grade = 'Poor'

print(f'{avg:.1f}')
print(grade)