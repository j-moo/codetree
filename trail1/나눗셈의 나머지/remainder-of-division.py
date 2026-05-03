A, B = map(int, input().split())

count_arr = [0] * 10

while A > 1:
    elem = A % B
    count_arr[elem] += 1

    A //= B

answer = 0
for i in range(10):
    answer += count_arr[i] ** 2

print(answer)