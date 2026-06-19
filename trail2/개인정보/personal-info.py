class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

N = 5
peoples = []

for _ in range(N):
    name, height, weight = input().split()
    height = int(height)
    weight = float(weight)

    peoples.append(People(name, height, weight))

peoples.sort(key=lambda x: x.name)
print('name')
for people in peoples:
    print(people.name, people.height, people.weight)

print()

peoples.sort(key=lambda x: -x.height)
print('height')
for people in peoples:
    print(people.name, people.height, people.weight)