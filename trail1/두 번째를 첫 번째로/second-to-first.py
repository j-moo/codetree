string = input()
string = list(string)
s = string[1]

for i in range(len(string)):
    if string[i] == s:
        string[i] = string[0]

print(''.join(string))