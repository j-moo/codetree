n = int(input())
arr = input().split()

answer = ''

for word in arr:
    for elem in word:
        answer += elem
        if len(answer) == 5:
            print(answer)
            answer = ''
    
print(answer)