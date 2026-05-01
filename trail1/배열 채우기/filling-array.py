N = 10
arr = list(map(int, input().split()))
answer = []

for elem in arr:
	if elem == 0:
		break
	
	answer.append(elem)

reversed_answer = reversed(answer)
print(*reversed_answer)