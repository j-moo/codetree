word1 = list(input())
word2 = list(input())

word1.sort()
word2.sort()

answer = 'Yes'
if len(word1) == len(word2):
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            answer = 'No'
else:
    answer = 'No'

print(answer)