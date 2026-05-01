N = int(input())

pass_cnt = 0
for _ in range(N):
	test = list(map(int, input().split()))

	sum_val = 0
	for score in test:
		sum_val += score
	
	avg = sum_val / 4

	if avg >= 60:
		print('pass')
		pass_cnt += 1
	else:
		print('fail')

print(pass_cnt)