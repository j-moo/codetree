N = int(input())

cnt = ord('A')

for i in range(1, N+1):
    for j in range(i):
        print(chr(cnt), end='')
        cnt += 1

        if cnt == 91:
            cnt = 65
    print()