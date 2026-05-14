string = input()
string = list(string)

string[1] = 'a'
string[-2] = 'a'

print(''.join(string))