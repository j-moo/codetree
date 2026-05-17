string = input()

for word in string:
    if word.isalpha() or word.isdigit():
        print(word.lower(), end='')