string = input()
target = input()

if target in string:
    print(string.index(target))
else:
    print(-1)