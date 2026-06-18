class Info:
    def __init__(self, name, house_number, region):
        self.name = name
        self.house_number = house_number
        self.region = region

n = int(input())

informations = []
for _ in range(n):
    name, house_number, region = input().split()
    informations.append(Info(name, house_number, region))

min_idx = 0
for idx in range(1, n):
    if informations[idx].name > informations[min_idx].name:
        min_idx = idx

print(f'name {informations[min_idx].name}')
print(f'addr {informations[min_idx].house_number}')
print(f'city {informations[min_idx].region}')