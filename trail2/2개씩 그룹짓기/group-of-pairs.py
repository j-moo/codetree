N = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = 2 * N - 1
answer = 0

while left < right:
    pair_sum = arr[left] + arr[right]
    answer = max(answer, pair_sum)

    left += 1
    right -= 1

print(answer)