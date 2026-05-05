N = int(input())
arr = list(map(int, input().split()))

max_idx = N
while max_idx > 0:
    curr_max = 0
    for i in range(max_idx):
        if arr[curr_max] < arr[i]:
            curr_max = i
    
    max_idx = curr_max
    print(max_idx+1, end=' ')