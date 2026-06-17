n = int(input())
arr = list(map(int, input().split()))

sorted_arr = []
for idx in range(1, n + 1):
    sorted_arr.append(arr[idx - 1])
    sorted_arr = sorted(sorted_arr)    
    if idx % 2 == 1:
        idx = idx // 2 + 1
        print(sorted_arr[idx - 1], end=' ')