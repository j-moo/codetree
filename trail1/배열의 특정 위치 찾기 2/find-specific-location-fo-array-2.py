N = 10
arr = list(map(int, input().split()))

even_sum = 0
odd_sum = 0
for idx in range(N):
    if (idx + 1) % 2 == 0:
        even_sum += arr[idx]
    else:
        odd_sum += arr[idx]

answer = max(odd_sum, even_sum) - min(odd_sum, even_sum)
print(answer)