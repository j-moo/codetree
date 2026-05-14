string = input()

string = list(string)
while len(string) > 1:
    index = int(input())

    if index >= len(string):
        string.pop()
    else:
        string.pop(index)
    
    print(''.join(string))