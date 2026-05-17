n = 0
arr = []

while True:
    string = input()

    if string.isdigit():
        break

    n += 1
    if n % 2 == 1:
        arr.append(string)

print(n)
for elem in arr:
    print(elem)