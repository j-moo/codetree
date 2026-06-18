class Inform:
    def __init__(self, date, dow, weather):
        self.date = date
        self.dow = dow
        self.weather = weather


n = int(input())

informs = []
for _ in range(n):
    date, dow, weather = input().split()
    informs.append(Inform(date, dow, weather))

min_idx = -1

for idx in range(n):
    if informs[idx].weather == 'Rain':
        if min_idx == -1 or informs[idx].date < informs[min_idx].date:
            min_idx = idx

print(f'{informs[min_idx].date} {informs[min_idx].dow} {informs[min_idx].weather}')