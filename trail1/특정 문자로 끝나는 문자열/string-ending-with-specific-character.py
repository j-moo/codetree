N = 10
arr = []

for _ in range(N + 1):
    string = input()
    arr.append(string)

flag = False
for i in range(N):
    if arr[i][-1] == arr[-1]:
        print(arr[i])
        flag =True

if not flag:
    print('None')