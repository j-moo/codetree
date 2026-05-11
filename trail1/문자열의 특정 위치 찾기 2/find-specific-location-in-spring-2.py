alpha = input()
arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']

cnt = 0
for word in arr:
    if word[2] == alpha or word[3] == alpha:
        print(word)
        cnt += 1

print(cnt)