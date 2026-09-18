N, K, P, T = map(int, input().split())

peoples = [False] * N
counts = [0] * N

peoples[P - 1] = True
counts[P - 1] = K

shake = [tuple(map(int, input().split())) for _ in range(T)]
shake.sort()

for t, x, y in shake:
    if peoples[x - 1] == True and peoples[y - 1] == True:
        counts[x - 1] -= 1
        counts[y - 1] -= 1
    elif peoples[x - 1] == True and counts[x - 1] > 0 and peoples[y - 1] == False:
        peoples[y - 1] = True
        counts[y - 1] = K
        counts[x - 1] -= 1
    elif peoples[y - 1] == True and counts[y - 1] > 0 and peoples[x - 1] == False:
        peoples[x - 1] = True
        counts[x - 1] = K
        counts[y - 1] -= 1

for i in peoples:
    print(int(i), end='')
