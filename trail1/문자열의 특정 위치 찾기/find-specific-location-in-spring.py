string, word = input().split()

if word in string:
    print(string.index(word))
else:
    print('No')