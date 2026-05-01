N = 8
arr = list(map(float, input().split()))

sum_val = 0
for elem in arr:
	sum_val += elem

avg = sum_val / N
print(f'{avg:.1f}')