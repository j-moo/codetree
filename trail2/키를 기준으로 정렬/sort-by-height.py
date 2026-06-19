class People():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

peoples = []

for _ in range(n):
    name, height, weight = input().split()
    height = int(height)
    weight = int(weight)
    
    peoples.append(People(name, height, weight))

peoples.sort(key=lambda x: x.height)

for people in peoples:
    print(f'{people.name} {people.height} {people.weight}')