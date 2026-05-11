a = input()
b = input()
c = input()

diff = max(map(len, (a, b, c))) - min(map(len, (a, b, c)))
print(diff)