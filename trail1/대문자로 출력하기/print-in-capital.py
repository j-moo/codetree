string = input()

for i in string:
    if i.isalpha():
        print(i.upper(), end='')