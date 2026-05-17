n = 2

answer = 0
for _ in range(2):
    string = input()

    number = ''
    for elem in string:
        if elem.isdigit():
            number += elem

    answer += int(number)

print(answer)