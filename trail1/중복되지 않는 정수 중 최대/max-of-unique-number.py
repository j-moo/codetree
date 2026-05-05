N = int(input())
arr = list(map(int, input().split()))

count_arr = [0] * (1001)

for elem in arr:
    count_arr[elem] += 1

answer = -1
for i in range(1001):
    if count_arr[i] == 1:
        answer = i
        
print(answer)