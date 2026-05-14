string = input()

string = string[:1] + string[2:len(string)-2] + string[len(string)-1:]
print(string)