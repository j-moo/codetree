n = int(input())

arr = []

for num in range(1, n + 1):
    x, y = map(int, input().split())
    
    dist = abs(0 - x) + abs(0 - y)

    arr.append((dist, num))

arr.sort(key=lambda x: (x[0], x[1]))

for dist, num in arr:
    print(num)