string = input()

cnt_1 = 0
cnt_2 = 0
for i in range(len(string)-1):
    if string[i] == 'e' and string[i+1] == 'e':
        cnt_1 += 1
    elif string[i] == 'e' and string[i+1] == 'b':
        cnt_2 += 1

print(cnt_1, cnt_2)