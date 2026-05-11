N = int(input())

cnt = 0
a_cnt = 0
for _ in range(N):
    string = input()

    cnt += len(string)

    if string[0] == 'a':
        a_cnt += 1

print(cnt, a_cnt)