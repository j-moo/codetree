string = input()

for word in string:
    if ord(word) >= ord('a'):
        print(word.upper(), end='')
    else:
        print(word.lower(), end='')
