n, k, t = input().split()
n, k = map(int, [n, k])

arr = []
for _ in range(n):
    string = input()

    flag = True
    for idx in range(len(t)):
        if t[idx] != string[idx]:
            flag = False
            break

    if flag:
        arr.append(string)

arr.sort()

print(arr[k - 1])