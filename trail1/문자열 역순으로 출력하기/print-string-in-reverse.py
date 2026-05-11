n = 4
arr = []

for _ in range(n):
    string = input()
    arr.append(string)

for word in arr[::-1]:
    print(word)