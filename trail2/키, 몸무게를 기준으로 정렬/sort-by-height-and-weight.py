class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
peoples = []

for _ in range(n):
    name, height, weight = input().split()
    height, weight = map(int, (height, weight))

    peoples.append(People(name, height, weight))

peoples.sort(key=lambda x: (x.height, -x.weight))

for people in peoples:
    print(people.name, people.height, people.weight)