string, n = input().split()
n = int(n)

for _ in range(n):
    Q = int(input())

    if Q == 1:
        string = string[1:] + string[0]
    elif Q == 2:
        string = string[-1] + string[:-1]
    else:
        string = string[::-1]

    print(string) 