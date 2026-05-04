N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(Q):
    quest = list(map(int, input().split()))

    if quest[0] == 1:
        idx = quest[1] - 1
        print(arr[idx])
    elif quest[0] == 2:
        for i in range(len(arr)):
            if arr[i] == quest[1]:
                print(i+1)
                break
        else:
            print(0)
    elif quest[0] == 3:
        s = quest[1] - 1
        e = quest[2] - 1
        for i in range(s, e + 1):
            print(arr[i], end=' ')
        print()