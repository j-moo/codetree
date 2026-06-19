class Number:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx


N = int(input())
arr = list(map(int, input().split()))

numbers = []

for i in range(N):
    numbers.append(Number(arr[i], i))

numbers.sort(key=lambda x: (x.value, x.idx))

answer = [0] * N

for new_idx in range(N):
    old_idx = numbers[new_idx].idx
    answer[old_idx] = new_idx + 1

print(*answer)