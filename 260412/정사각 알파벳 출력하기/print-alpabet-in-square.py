N = int(input())

cnt = ord('A')
for i in range(N):
    for j in range(N):
        print(chr(cnt), end='')
        cnt += 1
    print()