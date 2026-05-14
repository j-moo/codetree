string = input()
string = list(string)
a = string[0]
b = string[1]

for i in range(len(string)):
    if string[i] == a:
        string[i] = b
    elif string[i] == b:
        string[i] = a

print(''.join(string))