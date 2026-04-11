N = int(input())

cnt = ord('A')

for i in range(N):
    for j in range(N):
        if j >= i:
            print(chr(cnt), end=' ')
            cnt += 1
        else:
            print(' ', end=' ')
        
        if cnt == 91:
            cnt = 65
    print()