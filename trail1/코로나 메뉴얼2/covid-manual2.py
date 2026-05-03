N = 3

alpha_arr = [0] * 4

for _ in range(N):
    sym, temp = input().split()

    if sym == 'Y' and int(temp) >=37:
        alpha_arr[0] += 1
    elif sym == 'N' and int(temp) >= 37:
        alpha_arr[1] += 1
    elif sym == 'Y' and int(temp) < 37:
        alpha_arr[2] += 1
    elif sym == 'N' and int(temp) < 37:
        alpha_arr[3] += 1

for elem in alpha_arr:
    print(elem, end=' ')

if alpha_arr[0] >= 2:
    print('E')