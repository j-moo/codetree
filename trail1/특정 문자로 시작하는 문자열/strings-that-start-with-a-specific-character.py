N = int(input())
arr = []

for _ in range(N):
    string = input()
    arr.append(string)

alpha = input()

cnt = 0
sum_len = 0
for word in arr:
    if word[0] == alpha:
        cnt += 1
        sum_len += len(word)

avg = sum_len / cnt

print(f'{cnt} {avg:.2f}')