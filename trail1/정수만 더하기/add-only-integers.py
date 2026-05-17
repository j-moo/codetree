string = input()

sum_val = 0
for word in string:
    if word.isdigit():
        sum_val += int(word)

print(sum_val)