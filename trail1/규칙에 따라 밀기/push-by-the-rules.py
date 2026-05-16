string = input()
orders = list(input())

for order in orders:
    if order == 'R':
        string = string[-1] + string[:-1]
    else:
        string = string[1:] + string[0]
    

print(string)