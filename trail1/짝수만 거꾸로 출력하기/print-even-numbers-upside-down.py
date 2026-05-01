N = int(input())
arr = list(map(int, input().split()))

answer = []
for elem in arr[::-1]:
	if elem % 2 == 0:
		answer.append(elem)


print(*answer)	