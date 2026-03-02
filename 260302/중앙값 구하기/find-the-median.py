arr = list(map(int, input().split()))

if arr[0] > arr[1]:
    if arr[0] > arr[2]:
        arr[0], arr[2] = arr[2], arr[0]
    else:
        arr[0], arr[1] = arr[1], arr[0]
else:
    if arr[1] > arr[2]:
        arr[1], arr[2] = arr[2], arr[1]

print(arr[1])