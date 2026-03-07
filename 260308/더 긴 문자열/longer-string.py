# 두 개의 단어를 나눠서 리스트에 저장
text = input().split()

# 두 개의 단어 길이를 비교 하여 같다면 smae을 출력
if len(text[0]) == len(text[1]):
    print('same')

# 첫 번쨰 단어가 길다면 첫 번째 단어와 길이를 출력
elif len(text[0]) > len(text[1]):
    print(text[0], len(text[0]))

# 두 가지 경우가 아니라면(두 번째 단어가 큰 경우)두 번째 단어와 길이를 출력
else:
    print(text[1], len(text[1]))