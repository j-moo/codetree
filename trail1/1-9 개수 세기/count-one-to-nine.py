N = int(input())
arr = list(map(int, input().split()))

count_arr = [0] * 9

for elem in arr:
    count_arr[elem - 1] += 1

for count in count_arr:
    print(count)