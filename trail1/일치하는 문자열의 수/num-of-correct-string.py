n, A = input().split()

cnt = 0
for _ in range(int(n)):
    string = input()
    if string == A:
        cnt += 1

print(cnt)